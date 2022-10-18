<template>
  <div class="settings-content text-start">

    <section class="" v-if="this.profile">
      <h2>내 프로필</h2>
      <hr>
      <p>아이디 : {{ profile.username }}</p>
      <p>e-mail : {{ profile.email }}</p>
      <p>닉네임 : {{ profile.nickname }}</p>
      <router-link :to="{name: 'userUpdate'}"><button class="btn button-bg px-4">프로필 수정</button></router-link>
    </section>

    <section>
      <h2>기본 보안 설정</h2>
      <hr>
      <p>* 현재 비밀번호를 새 비밀번호로 바꿉니다.</p>
      <router-link :to="{name : 'changePassword'}">
        <button class="btn button-bg px-4">비밀번호 변경</button> 
      </router-link>
    </section>

    <section>
      <h2>회원 탈퇴</h2>
      <hr>
      <p>* 탈퇴 시 동일 유저 정보는 1년 간 회원 가입이 어렵습니다. 탈퇴를 진행하시겠습니까?</p>
      <button class="btn button-bg px-4" @click="signout">탈퇴</button>
    </section>
  </div>


</template>
 
<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SettingsProfileView',
  computed: {
    ...mapGetters(['profile']),
  },
  methods: {
    ...mapActions(['fetchProfile', 'signout'])
  },
  created() {
    this.fetchProfile()
  }
}
</script>

<style>
.settings-content {
  margin: 2em 2em 5em 2em;
  width: 80%;
}

.settings-content h1 > hr {
  border: 0;
  height: 3px;
}

.settings-content h2 {
  margin-top: 0em;
  margin-left: 0em;
}

.settings-content section {
  padding-left: 0em;
  margin-bottom: 4em;
}

.background {
  background-color: #fff
}

</style>
