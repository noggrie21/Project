<template>
  <div class="settings-auth container ">
    <div class="mb-4">
      <h2>로그인</h2>
    </div>

    <account-error-list></account-error-list>
    <p>MTV 계정으로 로그인</p>
    <form @submit.prevent="login(credentials)">

      <div class="settings-auth-input">
        <div>
          <label class="form-label text-start" for="username"></label>
          <input class="form-control p-1" v-model="credentials.username" type="text" id="username" 
          placeholder="아이디" required />
        </div>

        <div class="my-2">
          <label class="form-label" for="password"></label>
          <input class="form-control p-1" v-model="credentials.password" type="password" id="password" 
          placeholder="비밀번호" required />
        </div>

        <div class="my-3">
          <button class="btn button-bg px-4">로그인</button>
        </div>

      </div>
    </form>
  </div>
</template>

<script>
import { mapActions,mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList
  },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login']),
  }
}
</script>

<style>
.button-bg {
  background-color: rgb(254, 225, 90)
}
.settings-auth {
  margin-top: 5em; 
  width: 80%;
}
.settings-auth-input {
  width: 300px;
  margin: auto;
}
.settings-auth-input input {
  display: inline;
}
</style>