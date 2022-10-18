<template>
  <div class="comments-box">

    <review-comment-item
    v-for="comment in reversedComments"
    :key="comment.pk"
    
    :comment="comment"
    :reviewId="reviewId"
    :movieId="movieId"
    >
    </review-comment-item>
    

    <review-comment-list-form
    :reviewId="reviewId"
    @on-close="onClose">
    </review-comment-list-form>
  
  </div>
</template>

<script>
import ReviewCommentListForm from '@/components/ReviewCommentListForm.vue'
import ReviewCommentItem from '@/components/ReviewCommentItem.vue'
import _ from 'lodash'

export default {
  name: 'ReviewCommentList',
  components: {
    ReviewCommentListForm,
    ReviewCommentItem,
  },
  props: {
    comments: Array,
    reviewId: Number,
    movieId: Number,
  },
  computed: {
    reversedComments() {return _.orderBy(this.comments, 'created_at', 'desc')},
  },
  methods : {
    onClose() {this.$emit('on-close', false)} 
  }
}
</script>

<style>
.comments-box {
  background: rgba(249, 249, 249, 0.8);
  margin: 3px;
  padding-top: 5px;
  padding-bottom: 3px;
  padding-left: 15px;
  padding-right: 15px;
  border-radius: 5px;
}
</style>