<template>
  <div>
    <div>
      <h2 class="main-component-title ">최신 개봉작</h2>
    </div>
    <!-- <btn-goto-settings-check></btn-goto-settings-check> -->
    <p class="main-component-annotate m-0">* 내가 본 영화는 아래의 추천 영화에서 제외됩니다.</p>
    <p class="main-component-annotate">* <i class="fa-solid fa-trash-arrow-up"></i> 를 클릭하면 내가 본 영화에 추가됩니다.</p>
    <button @click="this.fetchNewMovies" class="yellow">최신순</button>
    <button @click="this.fetchPopularMovies" class="blue">인기순</button>
    <div class="main-component-content">
      <div class="row row-cols-2 row-cols-md-4 g-6">
        <new-movie-item
        v-for="(movie, index) in newMovies"
        :key="index"
        :movie="movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import NewMovieItem from '@/components/NewMovieItem.vue'
// import BtnGotoSettingsCheck from '@/components/BtnGotoSettingsCheck.vue'

export default {
  name: 'NewMovieList',
  components: {
    NewMovieItem, 
    // BtnGotoSettingsCheck
  },
  computed: {
    ...mapGetters(['newMovies']),
  },
  methods: {
    ...mapActions(['fetchNewMovies', 'fetchPopularMovies']),
  },
  created() {
    this.fetchNewMovies()
  }
}
</script>

<style scoped>
.yellow {
  background-color: rgb(254, 225, 90);
}
.blue {
  background-color: rgb(153, 201, 239);
}
button {
  margin: 5px;
  border: 0;
  outline: 0;
}

</style>