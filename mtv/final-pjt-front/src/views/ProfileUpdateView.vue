<template>
  <div class="settings-content text-start">

    <section>
      <h2>프로필 수정</h2>
      <hr>
      <p>
        <label for="email" class="form-label">E-mail</label>
        <input class="form-control" v-model="credentials.email" type="text" 
        placeholder="변경할 email을 입력해주세요" id="email" required />
      </p>

      <p>
        <label for="nickname" class="form-label">닉네임</label>
        <input class="form-control" v-model="credentials.nickname" type="text" 
        placeholder="변경할 닉네임을 입력해주세요" id="nickname" required />
      </p>

      <div class="my-4">
        <button class="btn button-bg px-4" @click="userUpdate(credentials)">수정</button>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ProfileUpdateView',
  data() {
    return {
      credentials: {
        email: '',
        nickname: ''
      }
    }
  },
  computed: {
    ...mapGetters(['profile']),
  },
  methods: {
    ...mapActions(['userUpdate'])
  },
  created() {
    this.profile()
  },
  // mounted() {
  //   this.email = this.profile.email
  //   this.nickname = this.profile.nickname
  //   console.log(this.nickname)
  //   console.log(this.currentUser.nickname)
  // }
}
</script>

<style>

</style>