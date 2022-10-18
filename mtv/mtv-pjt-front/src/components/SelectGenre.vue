<template>
  <div>
    <div>
      <h2 class="main-component-title">장르 추천작</h2>
    </div>
    <p class="main-component-annotate m-0">* 내가 본 영화는 아래의 추천 영화에서 제외됩니다.</p>
    <p class="main-component-annotate">* <i class="fa-solid fa-trash-arrow-up"></i> 를 클릭하면 내가 본 영화에 추가됩니다.</p>

    <select v-model="genrePk" class="form-control" @change="getGenreMovies(genrePk)">
      <option
      v-for="genre in genres"
      :key="genre.id" 
      :value="genre.id"
      >{{ genre.name }}
      </option>
    </select>

    <div class="main-component-content">
      <div class="row row-cols-2 row-cols-md-4 g-4">
        <select-genre-item
        v-for="(movie, index) in genreMovies"
        :key="index"
        :movie="movie">
        </select-genre-item>
      </div>
    </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SelectGenreItem from '@/components/SelectGenreItem.vue'

export default {
  name: 'SelectGenre',
  data() {
    return {
      genrePk: 35
    }
  },
  components: {
    SelectGenreItem,
  },
  computed: {
    ...mapGetters(['genres', 'genreMovies'])
  },
  methods: {
    ...mapActions(['getGenreMovies'])
  },
  created() {
    this.getGenreMovies(35)
  }
}
</script>

<style>

</style>