import Vue from 'vue'

import { VueMaterial } from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import Index from '@/Apps/Index.vue'

Vue.config.productionTip = false
Vue.use(VueMaterial)

new Vue({
  render: h => h(Index),
}).$mount('#app')
