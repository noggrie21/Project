<template>
  <div class="comment-form">
    <form @submit.prevent="onSubmit">
      <div class="d-flex justify-content-evenly article-input comment-input">
        <label for="form-label"></label>
        <input class="form-control form-control-article" type="text" placeholder="답글을 입력해주세요" v-model.trim="content" required>
        <div @click="onSubmit" class="btn article-btn">작성</div>
      </div>
    </form>
    <hr>


    <div class="comment-close">
      <span class="cursor-effect" @click="onClose">
        답글 창 닫기
      </span>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewCommentListForm',
  props: {
    reviewId: Number,
  },
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ movieId: this.movie.id, reviewId: this.reviewId, content: this.content, })
      this.content = ''
    },
    onClose() {this.$emit('on-close', false)}
  }
}
</script>

<style>
.comment-input {
  margin-bottom: 10px;
}
.comment-form {
  margin-top: 15px;
}
.comment-form > hr{
  margin: 5px;
}
.comment-close {
  padding: 5px;
}

</style>