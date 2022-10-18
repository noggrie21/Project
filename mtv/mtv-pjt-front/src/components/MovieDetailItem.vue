<template>
  <div class="">

    <div class="d-flex">
      <div class="detail-movie-poster">
        <img :src="movieImg" alt="" class="mx-3 py-3 detail-poster">
      </div>


      <article class="mx-3 py-3 text-start">
        <h1 class="py-3">{{ movie.title }}</h1>
        <p>개봉일 : {{ movie.release_date }}</p>
        <p>장르 : 
          <span v-for="(genre, index) in movie.genres" :key="index">{{ genre.name }} </span>
        </p>
        <p>평점 : {{ movie.vote_average }}</p>
        <p>{{ movie.overview }}</p>
      </article>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MovieDetailItem',
  props: {
    movie: Object,
  },
  computed: {
    ...mapGetters(['detailImgPath',]),
    movieImg() {return `${this.detailImgPath + this.movie.poster_path}`},
  },
}
</script>

<style>
.detail-movie-poster {
  height: 60vh;
  min-height: 250px;
}
.detail-poster {
  height: 100%;
}
</style>