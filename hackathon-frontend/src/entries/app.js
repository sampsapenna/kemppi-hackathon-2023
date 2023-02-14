import Vue from 'vue'
import VueRouter from 'vue-router'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


import TableSearch from '@/apps/App.vue'

import { app_router } from '@/common/router'

Vue.use(VueRouter)

Vue.config.productionTip = false
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


new Vue({  
  name: "main-application",
  router: app_router,
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
    },
  },
  created() {
    this.searched = this.users
  },
  ...TableSearch,
}).$mount('#app')
