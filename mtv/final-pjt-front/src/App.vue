<template>
  <div id="app" @scroll="handleScroll">
    <div v-if="watchedBtn" class="scrollTopMob d-flex">
      <router-link :to="{name: 'check'}">
        <button class="rounded-pill border scrollBtn mx-1">내가 본 영화 보러가기!</button>
      </router-link>
      <a href="#"><button class="rounded-circle border scrollBtn"><i class="fa-solid fa-arrow-up"></i></button></a>
    </div>
    <the-navbar></the-navbar>
    <!-- 스크롤 이동 -->
  </div>
</template>

<script>
import TheNavbar from './components/TheNavbar.vue'
import { mapActions, mapGetters } from 'vuex'

export default ({
  name: 'App',
  data() {
    return {
      watchedBtn: false
    }
  },
  components: {
    TheNavbar
  },
  methods: {
    ...mapActions(['currentingUser', 'fetchGenres']),
    handleScroll() {
      const scroll = window.scrollY
      if (scroll > 400) {
        this.watchedBtn = true
      } else {
        this.watchedBtn = false
      }
    }
  },

  beforeMount() {
    window.addEventListener("scroll", this.handleScroll)
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll)
  },

  getters: {
    ...mapGetters(['watchedMovies'])
  },
  created() {
    this.currentingUser()
    this.fetchGenres()
  },
})
</script>


<style>
.box {
  /* margin: 0px; */
  /* padding-top: 3px; */

  /* border-top: 2px solid rgb(38, 38, 38); */
}

#app {
  font-family: 'Noto Sans KR', 'Noto Serif KR', 'Nanum Gothic', serif; 
  font-size: 1.1rem;
  padding: 0px 0px 50px; 
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #626567;
  min-width: 700px;
  height: 1000px;
}

nav {
  padding: 15px;
}

nav a {
  font-weight: 700;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #99C9EF;
}

body {
  color: rgb(38, 38, 38);
}

a {
  text-decoration: none;
}

/* -- 메인 페이지(영화 카드) 시작-- */
.movie-card-poster {
  position: relative;
}

.movie-watch-button {
  position: absolute;
  bottom: 0;
	right: 0;
  padding: 3px;
  margin: 3px;
}

.card-img-top {
  width: 100%;
  border-top-left-radius: calc(.25rem - 1px);
  border-top-right-radius: calc(.25rem - 1px);
  border-bottom-left-radius: calc(.25rem - 1px);
  border-bottom-right-radius: calc(.25rem - 1px);
}

.card-body {
  padding: 0px;
}
/* -- 메인 페이지(영화 카드) 끝-- */


/* -- 디테일 페이지 (카드 슬라이드) 시작 -- */
.product {
  position: relative;
  overflow: hidden;
  padding: 20px;
}

.product-category {
  padding: 0 5vw;
  font-size: 30px;
  font-weight: 500;
  margin-bottom: 20px;
  text-transform: capitalize;
}

.product-container {
  padding: 0 10px;
  display: flex;
  overflow-x: auto;
  scroll-behavior: smooth;
  min-height: 250px;
}

.product-container::-webkit-scrollbar {
  display: none;
}

.product-card {
  flex: 0 0 auto;
  width: 120px;
  height: 160px;
  margin-right: 40px;
}

.product-image {
  position: relative;
  width: 100%;
  /* height: 350px; */
  overflow: hidden;
}

.product-thumb {
  width: 100%;
  height: 100%;
  /* object-fit: cover; */
}

.product-card:hover .card-btn {
  opacity: 1;
}

.product-info {
  width: 100%;
  height: 30px;
}

.product-brand {
  text-transform: capitalize ;
}

.product-short-description {
  width: 100%;
  height: 20px;
  line-height: 20px;
  overflow: hidden;
  opacity: 0.5;
  text-transform: capitalize;
  margin: 5px 0;
}

.pre-btn,
.nxt-btn {
  border: none;
  width: 10vw;
  height: 100%;
  position: absolute;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #fff 100%);
  cursor: pointer;
  z-index: 8;
}

.pre-btn {
  left: 0;
  transform: rotate(180deg);
}

.nxt-btn {
  right: 0;
}

.pre-btn img,
.nxt-btn img {
  opacity: 0.2;
}

.pre-btn:hover img,
.nxt-btn:hover img {
  opacity: 1;
}
.related-movies {
  min-height: 270px;
}
.movie {
  width: 150px;
  height: 230px;
}
.related-people p {
  font-size: 15px;
}
/* -- 디테일 페이지(카드 슬라이드) 끝 -- */


/* 스크롤 정의 */
.scrollTopMob {
  position: fixed;
  bottom: 50px; /* 아랫쪽 끝에서부터의 거리 */
  right: 30px; /* 오른쪽 끝에서부터의 거리 */
  z-index:99;
}

.scrollBtn {
  padding: 10px 18px 10px 18px;
  background-color: white;
}

</style>
