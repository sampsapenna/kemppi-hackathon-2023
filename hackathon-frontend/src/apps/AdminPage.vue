<template>
  <div>
    <nav class="navbar">
      <img id="navlogo" alt="navlogo" src="@/assets/kemppi_log_neg.png">
    </nav>
    <div id="adminroot">
      <router-view></router-view>
    </div>
  </div>
</template>

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

#adminroot {
  margin-top: 33px;
}
  
</style>
