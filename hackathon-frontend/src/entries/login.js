import Vue from 'vue'

import { VueMaterial } from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import IndexApp from '@/apps/Index.vue'

Vue.config.productionTip = false
Vue.use(VueMaterial)

new Vue({
  render: h => h(IndexApp),
}).$mount('#app')
