<template>
  <div id="customerfiles">
    <h2>
      Files for customer {{ $route.params.customer }}
    </h2>
    <b-button :to="`/app/${$route.params.username}/${$route.params.customer}/upload`">Upload files</b-button>
    <b-table
      sticky-header
      striped
      responsive
      head-variant="light"
      :items="items"
      :fields="fields"
    >
      <template #cell(name)="row">
        <b-link :href="`/api/${$route.params.username}/${$route.params.customer}/files/${row.item.name}`">
          {{ row.item.name }}
        </b-link>
      </template>
      <template #cell(actions)="row">
        <b-button
          style="margin-right: 1%;"
          variant="danger"
          @click="deleteFile(row.item.name)"
        >
          Delete
        </b-button>
      </template>    </b-table>
  </div>
</template>
  
<script>
export default {
  name: "FileTable",
  data: () => ({
    search: null,
    searched: [],
    items: [],
    fields: [
      {key: "name", label: "File name", sortable: true, sortDirection: "desc"},
      {key: "size", label: "File Size"},
      {key: "actions", label: "Actions"}
    ]
  }),
  mounted() {
    this.getFiles();
  },
  methods: {
    getFiles() {
      let path = `/api/${this.$route.params.username}/${this.$route.params.customer}/files`
      let url = new URL(path, window.location)
      
      fetch(url).then(resp => {
        console.log(resp);
        return resp.json();
      }).then(ret => {
        console.log(ret);
        this.items = ret;
      })
    },
    deleteFile(filename) {
      let path = `/api/${this.$route.params.username}/${this.$route.params.customer}/files/${filename}`
      let url = new URL(path, window.location)
      
      fetch(
        url,
        {
          method: "DELETE",
        }
      ).then(resp => {
        console.log(resp);
        this.getFiles();
      })
    }
  },
}
</script>

<style>
#customerfiles {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
  margin-right: 10%;
}
</style>
