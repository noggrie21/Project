import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
  state: {
    // Img 로드 시 필요한 데이터
    BASE_URL: 'https://www.themoviedb.org',  // img로드할 때 쓰는 기본 URL
    cardImgPath: '/t/p/w220_and_h330_face',  // 카드 사이즈 path
    detailImgPath: '/t/p/w600_and_h900_bestv2', // detail 사이즈 path

    // 장르 목록
    genres: {},
    genre: '',

    // 이미 본 영화
    watchedMovies: {},

    // 영화 관련 데이터
    newMovies: {},  // 최신 개봉작들
    action: null,

    sameDateMovies: {},  // 과거의 오늘 개봉작

    movie: {},  // 특정 영화
    reviews: {},

    genreMovies: {}, // 특정 장르 영화
  },

  getters: {
    // ImgPath: BASE_URL + 사이즈 별 Path
    cardImgPath: state => `${state.BASE_URL + state.cardImgPath}`,
    detailImgPath: state => `${state.BASE_URL + state.detailImgPath}`,

    genres: state => state.genres,
    genre: state => state.genre,

    watchedMovies: state => state.watchedMovies = {...state.watchedMovies},

    newMovies: state => state.newMovies,
    action: state => state.action,

    sameDateMovies: state => state.sameDateMovies,

    movie: state => state.movie,
    moviePk: state => state.movie.id,
    isMovie: state => !_.isEmpty(state.movie),

    reviews: state => state.reviews,
    isReviews: state => !_.isEmpty(state.reviews),

    genreMovies: state => state.genreMovies
  },

  mutations: {
    SET_GENRES: (state, genres) => state.genres = genres,
    SET_WATCHED_MOVIES: (state, watchedMovies) => state.watchedMovies = watchedMovies,
    SET_RECENT_NEW_MOVIE_LIST: (state, newMovies) => state.newMovies = newMovies,
    SET_SAMEDATE_MOVIE_LIST: (state, sameDateMovies) => state.sameDateMovies = sameDateMovies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_REVIEWS: (state, reviews) => state.reviews = reviews,
    SET_ACTION: (state, action) => state.action = action,
    SET_GENRE: (state, genre) => state.genre = genre,

    RESET_MOVIE: (state) => state.movie = {},

    SET_GENRE_MOVIE: (state, genreMovies) => state.genreMovies = genreMovies
  },

  actions: {
    // 본 영화 추가하기
    watchedAddMovie({commit, getters, dispatch }, {moviePk, action}) {
      axios({
        url: drf.movies.watchedAddMovie(moviePk), 
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_WATCHED_MOVIES', res.data) // 다만, 응답은 본 영화 목록 전체로 받음
          if (action === getters.action) {
            dispatch('fetchNewMovies')
          } else if ( action === 'new') {
            dispatch('fetchPopularMovies')
          } else if (action === 'genre') {
            console.log('도달성공')
            dispatch('getGenreMovies', getters.genre)
          } else {
            dispatch('fetchSameDateMovies')
          }
        })
        .catch(err => console.error(err.response))
    },

    // 장르 목록 받아오기
    fetchGenres({commit, getters}) {
      axios({
        url: drf.movies.genres(), 
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_GENRES', res.data)})
        .catch(err => console.error(err.response))
    },
    
    // 최신개봉작(최신순) 영화 데이터 받아오기
    fetchNewMovies({commit, getters}) {
      axios({
        url: drf.movies.recentNew(), 
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_RECENT_NEW_MOVIE_LIST', res.data)
          commit('SET_ACTION', 'new')
        })
        .catch(err => console.error(err.response))
    },

    // 최신개봉작(인기순) 영화 데이터 받아오기
    fetchPopularMovies({commit, getters}) {
      axios({
        url: drf.movies.recentPopular(), 
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_RECENT_NEW_MOVIE_LIST', res.data)
          commit('SET_ACTION', 'popular')
        })
        .catch(err => console.error(err.response))
    },


    setGenre({ commit }) {
      commit('SET_GENRE')
    },

    // 특정 영화 장르
    getGenreMovies({commit, getters}, genreId) {
      console.log(genreId)
      commit('SET_GENRE', genreId)
      axios({
        url: drf.movies.genreMovies(genreId), 
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res)
          commit('SET_GENRE_MOVIE', res.data)})
          commit('SET_ACTION', 'genre')
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },    
    // 과거의 오늘 개봉작 영화 데이터 받아오기
    fetchSameDateMovies({commit, getters}) {
      axios({
        url: drf.movies.sameDate(), 
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_SAMEDATE_MOVIE_LIST', res.data)})
        .catch(err => console.error(err.response))
      },

    // 특정 영화 데이터 받아오기
    fetchMovie({commit, getters}, movieId) {
      axios({
        url: drf.movies.detail(movieId), 
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_MOVIE', res.data)})
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    // 특정 영화의 댓글 받아오기
    fetchReviews({commit, getters}, movieId) {
      axios({
        url: drf.movies.reviews(movieId), 
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {commit('SET_REVIEWS', res.data)})
      .catch(err => console.error(err.response))
    },

    // 댓글(Review) 작성
    createReview({commit, getters}, {movieId, content}) {
      const review = { content }
      axios({
        url: drf.movies.reviews(movieId),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_REVIEWS', res.data)})
        .catch(err => {console.error(err.response)})
    },

    // 댓글(Review) 삭제
    deleteReview({commit, getters}, {movieId, reviewId}) {
      axios({
        url: drf.movies.review(movieId, reviewId),
        method: 'delete',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_REVIEWS', res.data)})
        .catch(err => {console.error(err.response)})
    },

    // 댓글(Review) 수정
    updateReview({commit, getters}, {movieId, reviewId, content}) {
      const review = { content }
      axios({
        url: drf.movies.review(movieId, reviewId),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_REVIEWS', res.data)})
        .catch(err => {console.error(err.response)})
    },

    // 댓글(Review) 좋아요
    likeReview({commit, getters}, {movieId, reviewId}) {
      axios({
        url: drf.movies.likeReview(movieId, reviewId),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_REVIEWS', res.data)})
        .catch(err => {console.error(err.response)})
    },

    // 답글(Comment) 작성
    createComment({commit, getters}, {movieId, reviewId, content}) {
      const comment = { content }
      axios({
        url: drf.movies.comments(movieId, reviewId),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_REVIEWS', res.data)})
        .catch(err => {console.error(err.response)})
    },

    // 답글(Comment) 수정
    updateComment({commit, getters}, {movieId, reviewId, commentId, content}) {
      const comment = { content }
      axios({
        url: drf.movies.comment(movieId, reviewId, commentId),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_REVIEWS', res.data)})
        .catch(err => {console.error(err.response)})
    },

    // 답글(Comment) 삭제
    deleteComment({commit, getters}, {movieId, reviewId, commentId}) {
      axios({
        url: drf.movies.comment(movieId, reviewId, commentId),
        method: 'delete',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_REVIEWS', res.data)})
        .catch(err => {console.error(err.response)})
    },

    // 영화 정보 리셋
    resetMovie({commit}) {commit('RESET_MOVIE')},

  },
}
  

