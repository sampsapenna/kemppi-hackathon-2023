<template>
  <div id="app">
    <nav class="navbar">
      <img id="navlogo" alt="navlogo" src="@/assets/kemppi_log_neg.png">
    </nav>
    <div class="login-page">
      <div class="container">
          <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
            <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
              <img id="logo" alt="logo" src="@/assets/kemppi_log_neg.png">
              <h1>Login</h1>
              <form action="/login" method="POST" class="form-group">
                <input v-model="emailLogin" name="username" type="username" class="form-control" placeholder="Username" required>
                <input v-model="passwordLogin" name="password" type="password" class="form-control" placeholder="Password" required>
                <input type="submit" class="btn btn-primary" value="Login">
                <p>Don't have an account? 
                  <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign up here</a>
                </p>
              </form>
            </div>

            <div v-else class="card register" v-bind:class="{ error: emptyFields }">
              <img id="logo" alt="logo" src="@/assets/kemppi_log_neg.png">
              <h1>Sign Up</h1>
              <form action="/login/register" method="POST" class="form-group">
                <input v-model="emailReg" name="username" type="username" class="form-control" placeholder="Username" required>
                <input v-model="passwordReg" type="password" class="form-control" placeholder="Password" required>
                <input v-model="confirmReg" name="password" type="password" class="form-control" placeholder="Confirm Password" required>
                <input type="submit" class="btn btn-primary" value="Sign up">
                <p>Already have an account? 
                  <a href="#" @click="registerActive = !registerActive, emptyFields = false">Login here</a>
                </p>
              </form>
            </div>
          </div>
        </div>

      </div>
    </div>
</template>

<script>
  export default {
    name: 'login-page',
    data() {
      return {
        input: {
          username: "",
          password: ""
        }
      }
    },
    methods: {
      login() {
        if (this.input.username != "" && this.input.password != "") {
          if (this.input.username == this.$parent.mockAccount.username && this.input.password == this.$parent
            .mockAccount.password) {
            this.$emit("authenticated", true);
            this.$router.replace({
              name: "secure"
            });
          } else {
            console.log("The username and / or password is incorrect");
          }
        } else {
          console.log("A username and password must be present");
        }
      }
    }
  }
</script>

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

  p {
    line-height: 1rem;
    color: #fff;
    font-size: ProximaNovaFont;
  }

  .card {
    padding: 5vh;
  }

  .card.login {
    background-color: #000;
    height: 80vh;
  }

  .card.register {
    background-color: #000;
    height: 80vh;
  }

  .form-group {
    align-items: center;
    margin-top: 10px;
    margin-bottom: 20px;
  }

  .form-control {
    margin-bottom: 20px;
  }

  .btn.btn-primary {
    text-align: center;
    margin-bottom: 20px;
    background-color: #fff;
    color: #000;
  }

  .login-page {
    justify-content: center;
    align-items: center;
    display: flex;
    height: 100vh;
  }

  h1 {
    margin-bottom: 1.5rem;
    text-align: center;
    color: #F57300;
    font-family: ProximaNovaFont;
  }
</style>