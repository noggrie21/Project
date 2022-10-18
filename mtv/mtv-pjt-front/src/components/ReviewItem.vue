<template>
  <div class="review-container">
    <div class="text-start d-flex justify-content-between">

      <!-- <div class="d-flex flex-column"> -->
      <div>
        <span class="review-user">{{ review.user.username }} </span>
        <span class="review-created-at">{{ timeInfo(review.created_at)}}</span>
      </div>
      <!-- </div> -->

      <div class="d-flex align-items-center">
        <div v-if="isReviewAuthor && !isEditing">
          <div class="btn article-btn" @click="switchIsEditing">수정</div>
          <div class="btn article-btn" @click="onDelete">삭제</div>
        </div>
      </div>
    </div>
    <p class="text-start review-content mb-0" v-if="!isEditing">{{ payload.content }}</p>
    <span v-if="isEditing"  class="d-flex flex-row">
      <input class="form-control form-control-article" type="text" v-model="payload.content">
      <div class="btn article-btn" @click="onUpdate">확인</div>
      <div class="btn article-btn" @click="switchIsEditing">취소</div>
    </span>

    <div class="d-flex justify-content-between">
      <!-- 답글 -->
      <span class="cursor-effect" @click="switchIsOpened">답글 {{commentCount}}</span>
      <div>

      </div>

      <!-- 좋아요 -->
      <div>
        <span>
          <button class="border-0 bg-white"
          @click="likeReview(payload)"
          >
          <span v-if="likeBtnMsg === 'good'">
            <i class="fa-solid fa-thumbs-up"></i>
            <!-- <span> 좋아요</span> -->
          </span>
          <span v-else>
            <i class="fa-regular fa-thumbs-up"></i>
            <!-- <span> 싫어요</span> -->
          </span>
          </button>
          {{ likeCount }}
        </span>
      </div>

    </div>
    <hr>

    <review-comment-list
    v-if="isOpened"
    :comments="review.comment_set"
    :reviewId="payload.reviewId"
    :movieId="payload.movieId"
    @on-close="onClose">
    </review-comment-list>



  </div>
</template>

<script>
import ReviewCommentList from '@/components/ReviewCommentList.vue'
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ReviewItem',
  components: {
    ReviewCommentList,
  },
  props: {
    review: Object,
    movieId: Number,
  },
  computed: {
    ...mapGetters(['movie','currentUser']),
    isReviewAuthor() {return this.currentUser.username === this.review.user.username},
    likeCount() {return this.review.liked_users?.length},
    likeBtnMsg() {
      const alreadyLike = this.review.liked_users.find((user) => this.currentUser?.username  === user.username)
      return alreadyLike ? 'good' : 'worth'
    },
    commentCount() {return this.review.comment_set?.length},
  },
  data() {
    return {
      isOpened: false,
      isEditing: false,
      payload: {
        movieId: this.movieId,
        reviewId: this.review.pk,
        content: this.review.content
      },
    }
  },
  methods: {
  ...mapActions(['deleteReview', 'updateReview', 'likeReview']),
    onDelete() {if (confirm('댓글을 삭제하시겠습니까?')) {this.deleteReview(this.payload)}},
    switchIsEditing() {this.isEditing = !this.isEditing},
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
      },
    switchIsOpened() {this.isOpened = !this.isOpened},
    timeInfo(time) {
    const d = new Date(time)
    return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate() + ". " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds()
    //  + ". " 
    // +  '일월화수목금토'.charAt(d.getUTCDay())+'요일'
    },
    onClose() {this.isOpened = !this.isOpened}
  },
}
</script>

<style>
.review-user {
  font-size: 22px;
  font-weight: 600;
}
.review-created-at {
  font-size: 15px;
  font-weight: 200;
}
.review-content {
  font-size: 22px;
  font-weight: 500;
}

.worth_button {
  background-color: rgb(254, 225, 90)
}
.like_button {
  background-color: rgb(153, 201, 239);
}
.cursor-effect:hover {
  cursor: pointer;
}
.review-container {
  padding: 10px 5px;
}
</style>