<template>
  <div class="col">
    <div class="card">
      <div class="card-body">
        <div class="movie-card-poster">
          <router-link :to="{ name: 'detail', params: { movieId: `${this.movieId}`} }" >
            <img class="card-img-top" :src="movieImg" alt="">
          </router-link>
          <div @click.stop="confirmMovie(movie)" class="px-2 btn checkbtn-bg movie-watch-button rounded-circle">
            <i class="fa-solid fa-trash-arrow-up"></i>
          </div>
        </div>
        <!-- <p class="card-text">{{ movie.title }}</p> -->
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'selectGenreItem',
  props: {
    movie: Object,
  },
  computed: {
    ...mapGetters(['cardImgPath']),
    movieImg() {return `${this.cardImgPath + this.movie.poster_path}`},
    movieId() {return this.movie.pk},
  },
  methods: {
    ...mapActions(['watchedAddMovie']),
    confirmMovie({pk, title}) {
      const payload = {
        moviePk: pk,
        action: 'genre',
        genrePk: pk
      }
      if (confirm(`추천 영화에서 ${title}을(를) 제외합니다.`)) {
        this.watchedAddMovie(payload)
      }
    }
  },
}
</script>

<style>

</style>