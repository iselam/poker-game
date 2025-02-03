import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import Vuelidate from 'vuelidate'
import VueMaterial from 'vue-material'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(Vuelidate)
Vue.use(VueMaterial)
Vue.use(VueAxios,axios)

export default axios

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
