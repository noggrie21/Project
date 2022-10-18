<template>
  <div class="container main-detail main-component">

    <movie-detail-item
    v-if="isMovie"
    :movie="movie"
    >
    </movie-detail-item>

    <movie-detail-people
    v-if="isMovie"
    :actors="movie.actors"
    :director="movie.director"
    :movieId="movie.id">
    </movie-detail-people>

    <review-list>
    </review-list>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieDetailItem from '@/components/MovieDetailItem.vue'
import MovieDetailPeople from '@/components/MovieDetailPeople.vue'
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'MovieDetailView',
  components: {
    MovieDetailItem,
    MovieDetailPeople,
    ReviewList,
  },
  computed: {
    ...mapGetters(['movie', 'isMovie']),
  },
  methods: {
    ...mapActions(['fetchMovie', 'fetchReviews']),
  },
  created() {
    const movieId = this.$route.params.movieId
    this.fetchMovie(movieId)
    this.fetchReviews(movieId)
  },
  watch: {
    $route(to, from) {
      if (to.path != from.path) {
        const movieId = this.$route.params.movieId
        this.fetchMovie(movieId)
        this.fetchReviews(movieId)
      }
    }
  }
}
</script>

<style>
.main-detail {
  padding-left: 5rem;
  padding-right: 5rem;
  padding-block-end: 5rem;
  padding-top: 3rem;
}
</style>