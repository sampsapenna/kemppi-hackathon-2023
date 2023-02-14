<template>
  <div id="customerfiles">
    <h2>
      Files for customer {{ $route.params.customer }}
    </h2>
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
    </b-table>
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
      {key: "size", lable: "File Size"},
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
