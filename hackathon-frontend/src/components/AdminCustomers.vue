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
          @click="console.log(`Deleting project ${row.item}`)"
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
      items: [
        {"customer": "admin"},
        {"customer": "test-customer"},
      ],
      fields: [
        {key: "customer", label: "Customer", sortable: true, sortDirection: "desc"},
        {key: "actions", label: "Actions"},
      ],
    }
  },
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
