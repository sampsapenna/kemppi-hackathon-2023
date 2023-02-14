<template>
  <div id="createuser">
    <h2>
      Add a new customer
    </h2>

    <form class="form-group">
      <input v-model="customer" name="customer" type="text" class="form-control" placeholder="Username" required>
      <input type="submit" class="btn btn-primary" value="Login" @click="addCustomer">
    </form>
  </div>
</template>
  
<script>
export default {
  name: "CreateCustomer",
  data() {
    return {
      customer: "",
    }
  },
  methods: {
    addCustomer() {
      let path = `/api/admin/admin/customers/${this.customer}`
      let url = new URL(path, window.location)
      fetch(
        url,
        {
          method: "PUT",
          credentials: "same-origin",
          headers: {
            "Content-Type": "application/json",
          },
        }
      ).then(resp => {
        console.log(resp);
        this.$router.push("/admin/customers");
      })
    },
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
