<template>
  <div>
    <div>
      <h2 class="main-component-title">과거의 오늘 개봉작 </h2>
    </div>
    <p class="main-component-annotate m-0">* 내가 본 영화는 아래의 추천 영화에서 제외됩니다.</p>
    <p class="main-component-annotate">* <i class="fa-solid fa-trash-arrow-up"></i> 를 클릭하면 내가 본 영화에 추가됩니다.</p>    
    <div class="main-component-content">
      <span class="main-component-annotate">(기준: {{ today }})</span>
      <div class="row row-cols-2 row-cols-md-4 g-4">

        <div v-for="(movie, index) in sameDateMovies"
        :key="index" class="col">
          <div class="card">
            <div class="card-body">
              <div class="movie-card-poster">
                <router-link :to="{ name: 'detail', params: { movieId: `${movie.pk}`} }">
                  <img :src="`${cardImgPath+movie.poster_path}`" alt="..." class="card-img-top" >
                </router-link>
                <div @click.stop="confirmMovie(movie)" class="px-2 btn checkbtn-bg movie-watch-button rounded-circle">
                  <i class="fa-solid fa-trash-arrow-up"></i>
                </div>
              </div>
              <!-- <p class="card-text">{{ movie.title }}</p> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
// import BtnGotoSettingsCheck from '@/components/BtnGotoSettingsCheck.vue'

export default {
  name: 'DateMovieList',
  components: {
    // BtnGotoSettingsCheck
  },
  computed: {
    ...mapGetters(['sameDateMovies', 'cardImgPath', 'watchedMovies']),
    today() {
      const today = new Date()
      const month = today.getMonth() + 1
      const date = today.getDate()
      return `${month}월 ${date}일`
    },

  },
  methods: {
    ...mapActions(['fetchSameDateMovies', 'watchedAddMovie']),
    confirmMovie({pk, title}) {
      const payload = {
        moviePk: pk,
        action: 'date',
      }
      if (confirm(`추천 영화에 ${title}을(를) 제외합니다.`)) {
        this.watchedAddMovie(payload)
      }
    },
  },
  created() {
    this.fetchSameDateMovies()
  }
}
</script>

<style>

</style>