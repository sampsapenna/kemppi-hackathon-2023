<template>
  <div>
    <nav class="navbar">
      <img id="navlogo" alt="navlogo" src="@/assets/kemppi_log_neg.png">
      <b-link id="logout" href="/logout">Logout</b-link>
    </nav>
    <div id="approot">
      <h1>Application and packages</h1>
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
@import '~mdb-ui-kit/css/mdb.min.css';

@font-face {
    font-family: ProximaNovaFont;
    src: url(@/assets/ProximaNovaFont.otf);
}

@font-face {
  font-family: MyriadProFont;
  src: url(@/assets/MYRIADPRO-REGULAR.OTF)
}

body {
  font-family: ProximaNovaFont;
}

.navbar {
  background-color: black;
  padding: 0;
}

#navlogo {
  height: 10%;
  width: 10%;
}

h1 {
  text-align: center;
  margin-top: 2em;
  margin-bottom: 1em;
}

#approot {
  margin-top: 33px;
}

#logout {
  margin-right: 20px;
  text-decoration: none;
  color: #ffff;
  font-size: 90%;
}

#logout:hover {
  text-decoration: none;
  color: #ffff;
}
</style>