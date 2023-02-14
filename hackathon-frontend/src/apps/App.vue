<template>
  <div>
    <nav class="navbar">
      <img id="navlogo" alt="navlogo" src="@/assets/kemppi_log_neg.png">
    </nav>
    <div>
      <router-view></router-view>
    </div>
  </div>
  
</template>

<script>
export default {
  name: 'TableSearch',
}
</script>

<style>
#app {
  justify-content: flex;
  align-items: flex;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.navbar {
    height: 33px;
    position: fixed;
    z-index: 2;
    top: 0;
    width: 100%;
    overflow: hidden;
    background-color: #000;
  }

#navlogo {
  height: 33px;
  background-size: 100%;
}
</style>
