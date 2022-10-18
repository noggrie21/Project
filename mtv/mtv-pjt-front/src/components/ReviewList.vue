<template>
  <div class="box review-container">
    <h2 class="text-start m-3">{{ movie.title }}'s 리뷰</h2>

    <review-list-form></review-list-form>

    <div v-if="isReviews">
      <review-item
      v-for="review in reversedReviews"
      :key="review.pk"
      :review="review"
      :movieId="movie.id">
      </review-item>
    </div>
  </div>

</template>

<script>
import ReviewItem from '@/components/ReviewItem.vue'
import ReviewListForm from '@/components/ReviewListForm.vue'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'ReveiwList',
  components: {
    ReviewItem,
    ReviewListForm,
  },
  computed: {
    ...mapGetters(['reviews', 'isReviews', 'movie']),
    reversedReviews() {return _.orderBy(this.reviews, 'created_at', 'desc')}
  },

}
</script>

<style>
.review-container {
  padding-left: 1rem;
  padding-right: 1rem;
}
.review-container > h2{
  padding-bottom: 1rem;
  border-bottom: 1.5px solid rgb(38, 38, 38);
}
</style>