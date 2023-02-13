<template>
  <div>
    <md-table v-model="searched" md-sort="name" md-sort-order="asc" md-card md-fixed-header>
      <md-table-toolbar>
        <div class="md-toolbar-section-start">
          <h1 class="md-title">Sovellukset</h1>
        </div>

        <md-field md-clearable class="md-toolbar-section-end">
          <md-input placeholder="Search by name..." v-model="search" @input="searchOnTable" />
        </md-field>
      </md-table-toolbar>

      <md-table-empty-state md-label="No users found"
        :md-description="`No user found for this '${search}' query. Try a different search term or create a new user.`">
        <md-button class="md-primary md-raised" @click="newUser">Create New User</md-button>
      </md-table-empty-state>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-sort-by="id" md-numeric>{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Name" md-sort-by="name">{{ item.name }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>



export default {
  name: 'TableSearch',
  data: () => ({
    search: null,
    searched: [],
    users: [
      {
        id: 1,
        name: "Sovellus 1",
      },
      {
        id: 2,
        name: "Sovellus 2",
      }
    ]
  }),
  methods: {
    newUser() {
      window.alert('Noop')
    },
    searchOnTable() {
      this.searched = this.searchByName(this.users, this.search)
    },

    toLower(text){
    return text.toString().toLowerCase()
    },

    searchByName(items, term){
    if (term) {
    return items.filter(item => this.toLower(item.name).includes(this.toLower(term)))
    }

  return items
}
  },
  created() {
    this.searched = this.users
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
