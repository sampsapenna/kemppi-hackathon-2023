import Vue from 'vue'
import VueRouter from 'vue-router'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import AdminPage from '@/apps/AdminPage.vue'

import { admin_router } from '@/common/router'

Vue.config.productionTip = false
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VueRouter)

new Vue({
  name: "AdminApplication",
  router: admin_router,
  data: () => ({
  }),
  methods: {
  },
  ...AdminPage,
}).$mount('#app')
