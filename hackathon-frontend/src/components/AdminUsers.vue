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
          :to="`/admin/users/passwd/${row.item.username}`"
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
      items: [],
      fields: [
        {key: "username", label: "Username", sortable: true, sortDirection: "desc"},
        {key: "actions", label: "Actions"},
      ],
    }
  },
  mounted() {
    this.getUsers()
  },
  methods: {
    getUsers() {
      let path = "/api/admin/admin/users"
      let url = new URL(path, window.location)

      fetch(url).then(resp => {
        return resp.json()
      }).then(ret => {
        this.items = ret.reduce((items, item) => {
          items.push({
            username: item,
          })
          return items
        }, [])
      })
    }
  }
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
