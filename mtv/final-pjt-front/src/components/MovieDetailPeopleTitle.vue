<template>
  <div class="product-card movie">

    <div class="product-image msg-none">

      <div v-if="movie.message" class="msg-expression">
        <div class="d-flex flex-column align-items-center">

          <p>
            {{ movie.person }}
          </p>
          <p>
            {{ movie.message }}
          </p>
        </div>
      </div>

      <div class="" v-else>
        <router-link  :to="{ name: 'detail', params: { movieId: `${movie.pk}`} }" >
          <img class="product-thumb" :src="`${cardImgPath+movie.poster_path}`" alt="...">
        </router-link>

        <div class="product-info">
          <p>{{ movie.title }}</p>
        </div>
      </div>
  </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetailPeopleTitle',
  props: {
    movie: Object,
  },
  computed: {
    ...mapGetters(['cardImgPath']),
  },
  methods: {
    ...mapActions(['fetchMovie']),
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
}

</script>

<style>
.msg-none {
  display: relative;
}
.msg-expression {
  font-size: 15px;
  display: absolute;
  width: 150px;
}
</style>