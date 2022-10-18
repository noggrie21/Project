<template>
  <div class="settings-content text-start">

    <account-error-list></account-error-list>
    
    <section>
      <h2>비밀번호 변경</h2>
      <hr>
      <p>
        <label class="form-label" for="old_password">현재 비밀번호 </label>
        <input class="form-control" v-model="credentials.old_password" type="password" id="old_password" required />
      </p>

      <p>
        <label class="form-label" for="new_password1">새 비밀번호</label>
        <input class="form-control" v-model="credentials.new_password1" type="password" id="new_password1" required />
      </p>
      
      <p>
        <label class="form-label" for="new_password2">새 비밀번호 확인</label>
        <input class="form-control" v-model="credentials.new_password2" type="password" id="new_password2" required />
      </p>

      <div class="my-4">
        <button class="btn button-bg px-4" @click="passwordChange(credentials)">비밀번호 변경</button>
      </div>
    </section>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'changePassword',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        new_password1: '',
        new_password2: '',
        old_password : '',
      }
    } 
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['passwordChange']),
  },
}
</script>

<style>

</style>
