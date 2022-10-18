<template>
  <div class="settings-content text-start">

    <h2 class="">내가 작성한 글</h2>
    <hr>

    <section>
      <div class="d-flex justify-content-evenly">
        <div>
          <p class="my-font-size">{{ review.length }}</p>
          <p>내가 작성한 댓글</p>
        </div>
        <div>
          <p class="my-font-size">{{ comment.length }}</p>
          <p>내가 작성한 답글</p>
        </div>
        <div>
          <p class="my-font-size">{{ comment.length }}</p>
          <p>내가 받은 좋아요 수</p>
        </div>
      </div>
    </section>

    <section>
      <h2 class="text-start">댓글 목록</h2>
      <hr>
      <div v-for="(article, index) in review" :key="`o-${index}`">
        <div class="d-flex flex-column">
          <div class="review d-flex justify-content-between">
            <div>
              <span>{{ index+1 }}.</span>
              <router-link :to="{ name: 'detail', params: {movieId: `${article.movie.pk}`} }">
                <span>
                  {{ article.content }} 
                </span>
              </router-link>   
            </div>

            <span><i class="fa-solid fa-thumbs-up"></i> {{ article.liked_users.length }}</span>
          </div>


          <!-- <div class="d-flex flex-column"> -->
          <p class="time-info text-start">

            <span class="article-time">작성 시간: {{timeInfo(article.created_at)}}  |  </span>
            <span class="article-time">수정 시간: {{timeInfo(article.updated_at)}}</span>
          </p>
          <!-- </div> -->
        </div>
      </div>
    </section>

    <section>
      <h2 class="">답글 목록</h2>
      <hr>
      <div v-for="(article,index) in comment" :key="index">
        <div>
          <span>{{ index+1 }}.</span>
          <router-link :to="{ name: 'detail', params: {movieId: `${article.review.movie}`} }">
            <span>
             {{ article.content }}
            </span>
          </router-link>
          <p class="time-info text-start">
            <span class="article-time">작성 시간: {{timeInfo(article.created_at)}}  |  </span>
            <span class="article-time">수정 시간: {{timeInfo(article.updated_at)}}</span>
            <!-- <p>{{timeInfo(article.created_at)}}</p> -->
          </p>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'articlesView',
  computed: {
    ...mapGetters(['articles']),
    review() {return _.orderBy(this.articles.review_set, 'created_at', 'desc')},
    comment() {return _.orderBy(this.articles.comment_set, 'created_at', 'desc')},
  },
  methods: {
    ...mapActions(['userArticles',]),
    timeInfo(time) {
      const d = new Date(time)
      return d.getFullYear() + ". " + (d.getMonth()+1) + ". " + d.getDate() + ". " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds()
      //  + ". " 
      // +  '일월화수목금토'.charAt(d.getUTCDay())+'요일'
    },
  },
  created() {
    this.userArticles()
  }
}
</script>

<style>
.my-font-size {
  font-size: 50px;
  text-align: center;
}
.article-time {
  font-size: 10px;
}
.review {
  margin-bottom: 3px;
}
.time-info {
  text-align: center;
  margin-left: 5px;
  /* line-height: 26px; */
}
 /* .head_article {
   padding: 20px 0 34px;
 }
 .title_list {
   padding: 20px 0 3px;
 }
 .section_orderlist{
    padding-top: 10px;
    border-bottom: 2px solid #333;
}
 .section_orderlist{
    position: relative;
    margin-top: 20px;
    padding: 0 20px;
    border: 1px solid #dddfe1;
}
.page_section {
    width: 1000px;
}
.name{
  font-size: 30px;
  font-weight: 700;
} */
</style>