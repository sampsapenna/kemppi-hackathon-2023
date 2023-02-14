<template>
  <div>
    <nav class="navbar">
      <img id="navlogo" alt="navlogo" src="@/assets/kemppi_log_neg.png">
    </nav>
    <router-view></router-view>
  </div>
</template>

<style>

@font-face {
    font-family: ProximaNovaFont;
    src: url(@/assets/ProximaNovaFont.otf);
  }

  @font-face {
    font-family: MyriadProFont;
    src: url(@/assets/MYRIADPRO-REGULAR.OTF)
  }

  .navbar {
    background-color: black;
    padding: 0;
  }

  #navlogo {
    height: 10%;
    width: 10%;
  }
  
</style>
