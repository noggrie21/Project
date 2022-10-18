const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'


export default {
  accounts: {
    // 로그인, 로그아웃, 회원가입
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // 현재 user 판단하는 Token
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',

    // 비밀번호 변경
    passwordChange: () => HOST + ACCOUNTS + 'password/change/',

    // 내 프로필 (get)
    myProfile: () => HOST + ACCOUNTS + 'detail/' ,
    signout: () => HOST + ACCOUNTS + 'detail/', // 유저 삭제 (delete)
    articles: () => HOST + ACCOUNTS + 'articles/', // 내가 작성한 글

    // 유저가 본 영화
    userWatched: () => HOST + ACCOUNTS + 'watchedmovies/',

  },
  movies: {
    genres: () => HOST + MOVIES + 'genres/',
    recentNew: () => HOST + MOVIES + 'recent-new/',
    recentPopular: () => HOST + MOVIES + 'recent-popular/',
    sameDate: () => HOST + MOVIES + 'samedate/',
    detail: (moviePk) => HOST + MOVIES + `${moviePk}/`,
    watchedAddMovie: (moviePk) => HOST + MOVIES + `${moviePk}/` + 'watch/',
    directorMovies: (moviePk, directorPk) => HOST + MOVIES + `${moviePk}/` + 'director/' + `${directorPk}/`,
    actorMovies: (moviePk, actorPk) => HOST + MOVIES + `${moviePk}/` + 'actor/' + `${actorPk}/`,
    reviews: (moviePk) => HOST + MOVIES + `${moviePk}/` + 'review/',
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + 'review/' + `${reviewPk}/`,
    likeReview: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + 'review/' + `${reviewPk}/` + 'like/',
    comments: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + 'review/' + `${reviewPk}/` + 'comment/',
    comment: (moviePk, reviewPk, commentPk) => HOST + MOVIES + `${moviePk}/` + 'review/' + `${reviewPk}/` + 'comment/' + `${commentPk}/`,
    bestReviews: () => HOST + MOVIES + 'bestreviews/',
    // 특정 장르 영화 
    genreMovies: (genrePk) => HOST + MOVIES + 'genredetail/' + `${genrePk}/`
  }
}
