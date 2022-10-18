<template>
  <div class="">

    <div>
      <h2 class="main-component-title">베스트 댓글 </h2>
    </div>

    <div class="main-component-content review-contaniner">
      <span class="main-component-annotate">(대상: 24시간 이내 작성된 댓글)</span>
      <div class="review-list">
        <div 
        class="d-flex justify-content-between review-item"
        v-for="(review, index) in bestReviews" :key="index">
          <p>
            {{index + 1}}위 <span>{{ review.user.username }}</span>님의  
            <router-link :to="{ name: 'detail', params: { movieId: `${review.movie.pk}`} }">
              '{{ review.content }}'
            </router-link>
          </p>
          <span class="like-count"><i class="fa-solid fa-thumbs-up"></i> {{ review.like_count }}</span>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import drf from '@/api/drf'
import axios from 'axios'

export default {
  name: 'BestReviewList',
  data() {
    return {
      bestReviews: null,
    }
  },
  computed: {},
  created() {
    axios({
      url: drf.movies.bestReviews(), 
      method: 'get',
    })
      .then(res => {this.bestReviews = res.data})
      .catch(err => console.error(err.response))
    },
  }

</script>

<style>
.review-contaniner {
  padding-left: 10px;
  padding-right: 10px;
}
/* .review-contaniner-hr {
  margin: 2px;
  height: 3px;
} */
.review-contaniner p {
  margin: 2px;
}
.review-contaniner p > span{
  font-weight: bold;
}
.like-count {
  font-size: 13px;
  font-weight: 200;
  line-height: 30px;
}
.review-list {
  padding: 3px;
  margin-top: 1rem;
  /* border: 1.7px solid #626567; */
}
.review-item {
  padding-right: 3px;
  border-bottom: 1.3px solid #626567;
}
</style>