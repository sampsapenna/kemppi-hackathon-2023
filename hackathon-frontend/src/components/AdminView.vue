<template>
  <div id="adminview">
    <h2>Administration</h2>
    <b-card
      title="Users"
      img-alt="Picture resembling a silhouette of a group of people"
      img-top
      tag="article"
      style="max-width: 80%;"
      class="mb-2"
    >
      <b-card-text>
        Manage users who can access the application.
      </b-card-text>

      <b-button
        to="/admin/users"
      >
        To user management
      </b-button>
    </b-card>
    <b-card
      title="Customers"
      img-alt="Picture resembling a silhouette of an office"
      img-top
      tag="article"
      style="max-width: 80%;"
      class="mb-2"
    >

    <b-card-text>
        Manage customers.
      </b-card-text>

      <b-button
        to="/admin/customers"
      >
        To customer management
      </b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "AdminView",
}
</script>

<style>
#adminview {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
  margin-right: 10%;
}
</style>
