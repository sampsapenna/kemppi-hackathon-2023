<template>
  <div id="createuser">
    <h2>
      Changing password for user {{ $route.params.username }}
    </h2>

    <form class="form-group">
      <input v-model="password" type="password" class="form-control" placeholder="Password" required>
      <input v-model="passwordConfirm" name="password" type="password" class="form-control" placeholder="Type passowrd again" required>
      <input type="submit" class="btn btn-primary" value="Update Password" @click="updatePassword">
    </form>
  </div>
</template>
  
<script>
export default {
  name: "ChangePassword",
  data() {
    return {
      password: "",
      passwordConfirm: "",
    }
  },
  methods: {
    updatePassword() {
      let path = `/api/admin/admin/users/${this.$route.params.username}`
      let url = new URL(path, window.location)
      fetch(
        url,
        {
          method: "PATCH",
          credentials: "same-origin",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            "password": this.passwordConfirm,
          }),
        }
      ).then(resp => {
        console.log(resp);
        this.$router.go(-1);
      })
    }
  }
}
</script>

<style>
#createuser {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
  margin-right: 10%;
}
</style>
