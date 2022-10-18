<template>
  <div>
    <nav class="d-flex justify-content-between nav-bg sticky-top">
      <a class="navbar-brand" href="/"><img src="@/assets/lo.png" alt="MTV logo" class="logo-img"></a>
      <ul class="nav justify-content-end">
        <li class="nav-item nav-link">
          <router-link to="/" class="" aria-current="page">홈</router-link>
        </li>
        <li class="nav-item nav-link">
          <router-link to="/settings/profile" class="">설정</router-link> 
        </li>
        <li v-if="!isLoggedIn" class="nav-item nav-link">
          <router-link to="/signup">회원가입</router-link>
        </li>
        <li v-if="!isLoggedIn" class="nav-item nav-link">
          <router-link to="/login">로그인</router-link>
        </li>
        <li v-if="isLoggedIn" class="nav-item nav-my-item logout">
          <span @click="logoutBtn">로그아웃</span>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'TheNavbar',
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  methods: {
    ...mapActions(['logout']),
    logoutBtn() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        this.$router.back()
      }
    }
  }
}
</script>

<style>
.nav-my-item {
  font-weight: 700;
  padding: 8px;
}
.logo-img {
  width: 100px;
  height: 40px;
  margin-left: 20px;
}
.logout {
  color: rgb(38, 38, 38);
}
.logout:hover {
  cursor: pointer;
  color: rgb(10, 88, 205);
}
.nav-bg {
  background-color: #f9f9f9;
}
</style>