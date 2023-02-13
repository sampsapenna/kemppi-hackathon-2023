<template>
  <div id="app">
    <div class="login-page">
      <transition name="fade">
        <div v-if="!registerActive" class="background-login"></div>
      </transition>
      <div class="background-register"></div>

      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
            <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
              <img alt="logo" src="@/assets/kemppi_log_neg.png">
              <h1>Login</h1>
              <form class="form-group">
                <input v-model="emailLogin" type="email" class="form-control" placeholder="Email" required>
                <input v-model="passwordLogin" type="password" class="form-control" placeholder="Password" required>
                <input type="submit" class="btn btn-primary" value="Login" @click="doLogin">
                <p>Don't have an account? <a href="#"
                    @click="registerActive = !registerActive, emptyFields = false">Sign up here</a>
                </p>
              </form>
            </div>

            <div v-else class="card register" v-bind:class="{ error: emptyFields }">
              <img alt="logo" src="@/assets/kemppi_log_neg.png">
              <h1>Sign Up</h1>
              <form class="form-group">
                <input v-model="emailReg" type="email" class="form-control" placeholder="Email" required>
                <input v-model="passwordReg" type="password" class="form-control" placeholder="Password" required>
                <input v-model="confirmReg" type="password" class="form-control" placeholder="Confirm Password"
                  required>
                <input type="submit" class="btn btn-primary" value="Sign up"> @click="doRegister">
                <p>Already have an account? <a href="#"
                    @click="registerActive = !registerActive, emptyFields = false">Login here</a>
                </p>
              </form>
            </div>
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
  p {
    line-height: 1rem;
    color: #fff;
  }

  .card {
    padding: 20px;
  }

  .card.login {
    background-color: #000;
    height: 90vh;
  }

  .card.register {
    background-color: #000;
    height: 90vh;
  }

  .form-group {
    margin-top: 10px;
    margin-bottom: 20px;
    align-items: center;
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
    align-items: center;
    display: flex;
    height: 100vh;
  }

  h1 {
    margin-bottom: 1.5rem;
    text-align: center;
    color: #F57300;
  }
</style>