<template>
  <div id="admincustomers">
    <div id="admincustomers-header">
      <h2>
        Customer administration
      </h2>

      <b-button
        to="/admin/customers/new"
      >
        Create customer entry
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
          variant="danger"
          @click="deleteCustomer(row.item.customer)"
        >
          Delete
        </b-button>
      </template>
    </b-table>
  </div>
</template>
    
<script>
export default {
  name: "AdminCustomers",
  data() {
    return {
      items: [],
      fields: [
        {key: "customer", label: "Customer", sortable: true, sortDirection: "desc"},
        {key: "actions", label: "Actions"},
      ],
    }
  },
  mounted() {
    this.getCustomers()
  },
  methods: {
    getCustomers() {
      let path = "/api/admin/admin/customers"
      let url = new URL(path, window.location)

      fetch(url).then(resp => {
        return resp.json()
      }).then(ret => {
        this.items = ret.reduce((items, item) => {
          items.push({
            customer: item,
          })
          return items
        }, [])
      })
    },
    deleteCustomer(customer) {
      let path = `/api/admin/admin/customers/${customer}`
      let url = new URL(path, window.location)
      
      fetch(url, {method: "DELETE"}).then(resp => {
        console.log("Deleted customer.")
        console.log(resp)
        this.getCustomers()
      })
    }
  }
}
</script>

<style>
#admincustomers {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
  margin-right: 10%;
}
</style>
