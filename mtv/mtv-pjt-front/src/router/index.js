import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import MainPageView from '../views/MainPageView.vue'
import SettingsView from '../views/SettingsView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SettingsProfileView from '../views/SettingsProfileView.vue'
import SettingsCheckView from '../views/SettingsCheckView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import changePasswordView from '../views/changePasswordView.vue'
import NotFound404 from '../views/NotFound404.vue'
import articlesView from '../views/articlesView.vue' 
import ProfileUpdateView from '../views/ProfileUpdateView.vue' 


Vue.use(VueRouter)

const routes = [
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404',
    name:'NotFound'
  },
  {
    path: '/',
    name: 'MainPageView',
    component: MainPageView,
  },
  {
    path: '/movies/:movieId',
    name: 'detail',
    component: MovieDetailView,
  },
  {
    path: '/settings',
    name: 'Settings',
    component: SettingsView,
    children: [
      {
        path: '/settings/profile',
        name: 'profile',
        component: SettingsProfileView
      },
      // 프로필 수정
      { 
        path: '/settings/profile',
        name: 'userUpdate',
        component: ProfileUpdateView
      },
      {
        path: '/settings/checkmovie',
        name: 'check',
        component: SettingsCheckView
      },
      // 비밀번호 변경
      {
        path: '/settings/profile',
        name: 'changePassword',
        component: changePasswordView
      },
      {
        path: '/settings/articles',
        name: 'articles',
        component: articlesView
      },
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  scrollBehavior() { 
    return { x: 0, y: 0 } 
  },
  routes
})

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup', 'MainPageView',]

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('해당 페이지로 이동하려면 로그인을 해야합니다.')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'MainPageView' })
  }
})

export default router
