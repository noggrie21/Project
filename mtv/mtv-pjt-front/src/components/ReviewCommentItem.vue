<template>
  <div class="comment-container">
    <div class="text-start d-flex justify-content-between">
      <!-- 답글 유저이름 & 생성 시간 -->
      <div>
        <span class="review-user">{{ comment.user.username }} </span>
        <span class="review-created-at">{{ timeInfo(comment.created_at)}}</span>
      </div>
      <!-- 수정 및 삭제 버튼 -->
      <div class="d-flex align-items-center">
        <span v-if="isReviewAuthor && !isEditing">
          <div class="btn article-btn" @click="switchIsEditing">수정</div>
          <div class="btn article-btn" @click="onDelete">삭제</div>
        </span>
      </div>
    </div>
  <!-- 답글 내용 -->
  <p class="text-start mb-0" v-if="!isEditing">{{ payload.content }}</p>
  <span v-if="isEditing" class="d-flex flex-row form-control-article-container" >
    <input class="form-control form-control-article" type="text" v-model="payload.content">
    <div class="btn article-btn" @click="onUpdate">확인</div>
    <div class="btn article-btn" @click="switchIsEditing">취소</div>
  </span>
  <hr class="comment-content-under">
  </div>


    
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'ReviewCommentItem',
  props: {
    comment: Object,
    reviewId: Number,
    movieId: Number,
  },
  data() {
    return {
      isEditing: false,
      payload: {
        movieId: this.movieId,
        reviewId: this.reviewId,
        commentId: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    isReviewAuthor() {return this.currentUser.username === this.comment.user.username},
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {this.isEditing = !this.isEditing},
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
    onDelete() {if (confirm('답글을 삭제하시겠습니까?')) {this.deleteComment(this.payload)}},
    timeInfo(time) {
    const d = new Date(time)
    return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate() + ". " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds()
    },
  },
}
</script>

<style>
.comment-container {
  padding: 5px 0px;
}
.comment-container > p{
  padding-top: 3px;
  padding-left: 3px;
  padding-bottom: 3px;
}
.comment-content-under {
  margin-top: 5px;
  margin-bottom: 3px;
}
</style>