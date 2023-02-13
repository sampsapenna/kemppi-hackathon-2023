<template>
  <div>
    <nav class="navbar">
      <img id="logo" alt="Kemppi logo" src="@/assets/Kemppi_logo.png">
    </nav>
    <router-view></router-view>
  </div>
</template>

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
  background-color: black;
}

#logo {
  height: 20%;
  width: 20%;
}
</style>
