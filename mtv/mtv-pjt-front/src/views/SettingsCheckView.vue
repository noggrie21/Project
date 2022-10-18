<template>
  <div class="settings-content text-start">
    <div class="">
      <h2 class="">내가 본 영화</h2>
      <hr>
      <p class="">* 해당 페이지의 영화들은 메인 페이지에 보이지 않습니다.</p>
      <p class="">* <i class="fa-solid fa-boxes-packing"></i> 를 클릭하면 메인 페이지의 추천 영화에 포함됩니다.</p>
    </div>

    <div class="watched-list">
      <div class="row row-cols-1 row-cols-md-6 g-6">
        <div v-for="(movie, index) in this.watchedMovies" :key="index"> 
          <div class="col">
            <div class="card">
              <div class="card-body">
                <div class="movie-card-poster">
                  <img class="card-img-top" :src="`${movieImg + movie.poster_path}`" alt="">
                  <div @click="confirmMovie(movie)" class="px-1 btn checkbtn-bg movie-watch-button rounded-circle">
                    <i class="fa-solid fa-boxes-packing"></i>
                  </div>
                </div>
                <p class="card-text">{{ movie.title }}</p>
              </div>
            </div>
          </div>
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SettingsCheckView',
  computed: {
    ...mapGetters(['watchedMovies', 'cardImgPath']),
    movieImg() {return `${this.cardImgPath}`},
  },
  methods: {
    ...mapActions(['userWatched', 'watchedAddMovie']),
    confirmMovie({pk, title}) {
      const payload = {
        moviePk: pk,
        action: 'settings',
      }
      if (confirm(`추천 영화에 ${title}을(를) 포함합니다.`)) {
        this.watchedAddMovie(payload)
      }
    }
  },
  created() {
    this.userWatched()
  }
}
</script>

<style>

</style>