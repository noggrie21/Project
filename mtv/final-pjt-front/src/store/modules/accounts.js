import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    authError: null,
    profile: {},
    articles: {},
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}` }),
    profile: state => state.profile,
    isProfile() { return !_.isEmpty(this.profile)},
    articles: state => state.articles,
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_ARTICLES: (state, articles) => state.articles = articles
  },
  actions: {
    saveToken({commit}, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({commit}) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    // credentails : 사용자 입력 정보
    signup({commit, dispatch}, credentials) {
      axios({
        url: drf.accounts.signup(), 
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key 
          dispatch('saveToken', token)
          dispatch('currentingUser')
          router.push({ name: 'MainPageView' })
        })
        .catch(err => {
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    // 로그인
    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('currentingUser')
          router.push({ name: 'MainPageView' })
        }) 
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    // 로그아웃
    logout({getters, dispatch}) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          router.push({ name: 'MainPageView' }) 
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    // 현재 로그인한 유저
    currentingUser({commit, getters, dispatch}) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
            console.error(err.response)
          })
      }
    },

    // 비밀번호 변경
    passwordChange({getters}, credentials) {
      axios({
        url: drf.accounts.passwordChange(),
        method: 'post',
        data: credentials,
        headers: getters.authHeader,
      })
        .then(() => {
          router.push({ name: 'MainPageView' })
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    // 회원 탈퇴
    signout({ getters, dispatch }) {
      if (confirm('정말 탈퇴하시겠습니까?')) {
        axios({
          url: drf.accounts.signout(),
          method: 'delete',
          headers: getters.authHeader
        })
          .then(() => {
            dispatch('removeToken')
            router.push({ name: 'MainPageView' }) 
          })
          .catch(err => {
            console.error(err.response)
          })
      }
    },

    // 내 프로필
    fetchProfile({ commit, getters} ) {
      axios({
        url: drf.accounts.myProfile(),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {commit('SET_PROFILE', res.data)})
        .catch(err => {
          console.error(err.response)
        })
    },
    // 세팅 페이지 접속 시 본 영화 목록 갱신
    userWatched({commit, getters}) {
      axios({
        url: drf.accounts.userWatched(), 
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_WATCHED_MOVIES', res.data)})
        .catch(err => console.error(err.response))
    },

    // 내가 작성한 글들
    userArticles({ commit, getters } ) {
      axios({
        url: drf.accounts.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_ARTICLES', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    // 프로필 수정
    userUpdate({ getters }, credentials ) {
      axios({
        url: drf.accounts.myProfile(),
        method: 'put',
        data: credentials,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res)
          router.push({ name: 'profile' })
        })
        .catch(err => {
          alert('양식에 맞지 않습니다.')
          console.error(err.response)
        })
    }
  }
}

