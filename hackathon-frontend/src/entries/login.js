import Vue from 'vue'
import Index from '@/Apps/Index.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(Index),
}).$mount('#app')
