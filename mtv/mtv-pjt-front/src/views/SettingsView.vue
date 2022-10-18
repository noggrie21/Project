<template>
  <div class="d-flex">
      <nav class="d-flex flex-column settings-nav">
        <router-link :to="{ name: 'profile' }">마이 페이지</router-link>
        <router-link :to="{ name: 'check' }">내가 본 영화</router-link>
        <router-link :to="{ name: 'articles'}">내가 작성한 글</router-link>
      </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'SettingsView',
}
</script>

<style>
.nowarp{white-space:nowrap;}

.asd {
  width: 300px;
}
.height {
  height: 800px;
  margin: 0;
}
.settings-nav{
  min-width: 170px;
  color: #333;
  border-right: 1px solid #e5e5e5;
  background: #f9f9f9;
  min-height: 1000px;
}
.settings-nav > a {
  margin-top: 20px;
}

.tbl_model {
  position: relative;
  width: 100%;
  table-layout: fixed;
  border-spacing: 0;
  border-collapse: collapse;
  word-wrap: break-word;
  word-break: keep-all;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
.blind {
  position: absolute;
  clip: rect(0 0 0 0);
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
}
</style>