<template>
  <div class="review-container">
    <form @submit.prevent="onSubmit">
      <div class="d-flex justify-content-between article-input">
        <input class="form-control form-control-article" type="text" placeholder="댓글을 입력해주세요" v-model.trim="content" required>
        <div class="btn article-btn" @click="onSubmit">작성</div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListForm',
  props: {
    review: Object,
    action: String,
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
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ movieId: this.movie.id, content: this.content, })
      this.content = ''
    },
  }
}
</script>

<style>
.article-input {
  max-height: 38px;
}
.form-control-article {
  max-width: 95%;
  margin-left: 5px;
  margin-right: 5px;
}
.form-control-article-container {
  margin-top: 7px;
}
.article-btn {
  width: 50px;
  padding: 6px;
}
</style>