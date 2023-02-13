<template>
  <div id="adminusers">
    <div id="adminusers-header">
      <h2>
        User administration
      </h2>

      <b-button
        to="/admin/users/new"
      >
        Create user
      </b-button>
    </div>

    <b-table
      sticky-header
      striped
      responsive
      head-variant="light"
      :items="items"
      :fields="fields"
    >
      <template #cell(actions)="row">
        <b-button
          style="margin-right: 1%;"
          @click="console.log(`Restoring password for ${row.item}`)"
        >
          Restore password
        </b-button>
        <b-button
          style="margin-right: 1%;"
          :to="`/admin/users/edit/${row.item.username}`"
        >
          Edit user
        </b-button>
        <b-button
          variant="danger"
          @click="console.log(`Deleting user ${row.item}`)"
        >
          Delete
        </b-button>
      </template>
    </b-table>
  </div>
</template>
  
<script>
export default {
  name: "AdminUsers",
  data() {
    return {
      items: [
        {"username": "admin"},
        {"username": "test-user"},
      ],
      fields: [
        {key: "username", label: "Username", sortable: true, sortDirection: "desc"},
        {key: "actions", label: "Actions"},
      ],
    }
  },
}
</script>

<style>
#adminusers {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
  margin-right: 10%;
}
</style>
