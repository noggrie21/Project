<template>
  <div v-if="isMovie">
    <!-- <h1>moviedetailpeople</h1> -->


    <div class="related-people d-flex justify-content-between">
      <!-- 영화감독 -->
      <div class="product">

        <h2 class="p-0 product-category">감독</h2>

        <div v-if="isImg(director)">
          <img :src="`${cardImgPath+director.profile_path}`" alt="" class="profile cursor-effect" @click="fetchDirectorMoives(director.id)">
          <p>{{ director.name }}</p>
        </div>

        <div v-else>
          <img  :src="profile" alt="" class="profile">
          <p>{{ director.name }}</p>
        </div>
      </div>

      <!-- 영화배우 -->
      <div class="product"> 
        <h2 class="product-category">출연진</h2>
        <button class="pre-btn">></button>
        <button class="nxt-btn">></button>

        <div class="product-container">
          <div class="product-card" v-for="(actor, index) in actors" :key="index" >
            <!-- 배우 이미지 -->
            <div class="product-image">
              <img v-if="isImg(actor)" :src="`${cardImgPath+actor.profile_path}`" class="product-thumb cursor-effect" alt="" @click="fetchActorMoives(actor.id)">
              <img v-else :src="profile" alt="" class="profile">
            </div>
            <!-- 배우 정보 -->
            <div class="product-info">
              <p class="product-brand">{{ actor.name }}</p>
            </div>
          </div>
        </div>

      </div>

    </div>




    <div class="product"> 
        <h2 class="product-category">관련 영화</h2>
        <button class="pre-btn">></button>
        <button class="nxt-btn">></button>

        <div v-if="isMovies" class="product-container related-movies">

          <movie-detail-people-title
          v-for="(movie, index) in relatedMovies" :key="index"
          :movie="movie"
          >
          </movie-detail-people-title>
            
        </div>
    </div>
  </div>

</template>

<script>
import MovieDetailPeopleTitle from '@/components/MovieDetailPeopleTitle.vue'
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  name: 'MovieDetailPeople',
  components: {
    MovieDetailPeopleTitle,
  },
  data() {
    return {
      profile : 'https://han.gl/jOrrz',
      relatedMovies: null,
    }
  },
  props: {
    actors: Array,
    director: Object,
    movieId: Number,
  },
  computed: {
    ...mapGetters(['movie', 'cardImgPath', 'isMovie']),
    isMovies() {return !_.isEmpty(this.relatedMovies)},
  },
  methods: {
  ...mapActions(['resetMovie']),
    isImg(person) {return !_.isEmpty(person.profile_path)},
    // 감독의 추가 영화 정보 가져오기
    fetchDirectorMoives(directorId) {
      axios({
        url: drf.movies.directorMovies(this.movieId, directorId),
        method: 'get',
      })
        .then(res => {this.relatedMovies = res.data.length? res.data : Array(res.data)})
        .catch(err => {console.error(err.response)})
    },
    // 배우의 추가 영화 정보 가져오기
    fetchActorMoives(actorId) {
      axios({
        url: drf.movies.actorMovies(this.movieId, actorId),
        method: 'get',
      })
        .then(res => {this.relatedMovies = res.data.length? res.data : Array(res.data)})
        .catch(err => {console.error(err.response)})
    },
    resetMovie() {this.resetMovie()}
  },
  created() {
    this.fetchDirectorMoives(this.director.id)
  },
  mounted() {
    const productContainers = [...document.querySelectorAll('.product-container')]
    const nxtBtn = [...document.querySelectorAll('.nxt-btn')]
    const preBtn = [...document.querySelectorAll('.pre-btn')]

    productContainers.forEach((item, i) => {
        let containerDimensions = item.getBoundingClientRect()
        let containerWidth = containerDimensions.width

        nxtBtn[i].addEventListener('click', () => {
            item.scrollLeft += containerWidth;
        })

        preBtn[i].addEventListener('click', () => {
            item.scrollLeft -= containerWidth;
        })
    })
  },
  watch: {
    movie() {
      this.$router.beforeEach
      this.fetchDirectorMoives(this.movie.director.id)
    }
  }
}
</script>

<style>
.profile {
  width: 120px;
  height: 180px;
}
</style>