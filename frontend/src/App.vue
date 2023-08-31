<template>
  <div class="app">
    <LoginSecond></LoginSecond>
    <router-view></router-view>
  </div>
</template>

<script>
import LoginSecond from './components/LoginSecond.vue'
export default {
  name: 'App',
  components: {
    LoginSecond
  },

  data() {
    return {
      userName: '',
      userAccount: '',
    }
  },

  methods:{
    changePage() {
      this.$router.push({ path: '/education', query: {userName: this.userName, userAccount: this.userAccount}})
    }
  }
}
</script>

<style>
.app {
  height: 100%;
  width: 100%;
  background: url(./assets/login_bg.png);
  background-position: center;
  background-size: cover;
  position: fixed;
}
</style>
