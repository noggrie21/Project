<template>
  <div class="settings-auth container">
    <div class="mb-4">
      <h3>회원 가입</h3>
    </div>
    <account-error-list v-if="authError"></account-error-list>
    <p>회원 가입으로 MTV를 마음껏 즐겨 보세요!!</p>
    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username"> </label>
        <input class="p-1" v-model="credentials.username" type="text" id="username" 
        placeholder="아이디" required />
      </div>

      <div class="my-2">
        <label for="password1"> </label>
        <input class="p-1" v-model="credentials.password1" type="password" id="password1" 
        placeholder="비밀번호" required />
      </div>

      <div>
        <label for="password2"></label>
        <input class="p-1" v-model="credentials.password2" type="password" id="password2" 
        placeholder="비밀번호 재확인" required />
      </div>

      <div class="my-3">
        <button class="btn button-bg px-4">회원가입</button>
      </div>
    </form>
  </div>

</template>
 
<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'SignupView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>
.button-bg {
  background-color: rgb(254, 225, 90)
}
.settings-auth {
  margin-top: 5em; 
}
</style>