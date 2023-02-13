import Vue from 'vue'

import { VueMaterial } from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'


import TableSearch from '@/apps/App.vue'

Vue.config.productionTip = false
Vue.use(VueMaterial)

new Vue({
  render: h => h(TableSearch),
  

}).$mount('#app')
