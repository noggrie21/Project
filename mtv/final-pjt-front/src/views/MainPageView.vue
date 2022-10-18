<template>
  <div class="main container">

    <new-movie-list class="main-component"></new-movie-list>
    <date-movie-list class="main-component"></date-movie-list>
    <select-genre class="main-component"></select-genre>
    <best-review-list class="main-component"></best-review-list>
  </div>
</template>

<script>
import SelectGenre from '@/components/SelectGenre.vue'
import DateMovieList from '@/components/DateMovieList.vue'
import BestReviewList from '@/components/BestReviewList.vue'
import NewMovieList from '@/components/NewMovieList.vue'



export default {
  name: 'MainPageView',
  components : {
    SelectGenre, DateMovieList , BestReviewList, NewMovieList
  }
}
</script>

<style>
/* 메인 페이지 - 자식 컴포넌트 규격 */
.main-component {
  margin-block-start: 3rem;
  margin-block-end: 12rem;
  /* padding-bottom: rem; */
  /* margin-left: 10rem; */
  /* margin-right: 10rem;/ */
}
.main {
  padding-left: 10rem;
  padding-right: 10rem;
  padding-block-end: 0.5rem;
}
.main-component-title {
  display: inline-block;
  margin: 1rem;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  padding-bottom: 10px;
  border-bottom: 2px solid #626567;
}
.main-component-content {
  width: 100%;
  margin: auto;
}
.main-component-annotate {
  font-weight: 300;
  font-size: 15px;
  text-align: right;
  display: block;
  margin-block-end: 10px;
}
.col {
  padding: 0px 8px 0px;
}
.card {
  /* margin-bottom: 10px; */
  margin-top: 10px;
  margin-bottom: 17px;
  word-wrap: break-word;
  /* border: 1px solid black; */
  /* width: 100px; */
  /* height: 50px; */
  text-overflow:ellipsis;
  /* white-space: nowrap; */
  box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;
  margin-left: 10px;
}
</style>