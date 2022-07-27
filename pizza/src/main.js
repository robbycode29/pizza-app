import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import './assets/tailwind.css'
import './index.css'


import LoginPage from './components/LoginPage.vue'
import ClientPage from './components/client/ClientPage.vue'
import AdminPage from './components/admin/AdminPage.vue'

import FoodMenu from './components/client/client-components/FoodMenu.vue'
import OrderHistory from './components/client/client-components/OrderHistory.vue'
import ShoppingCart from './components/client/client-components/ShoppingCart.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [

  // home and auth page

  { path: '/', component: LoginPage },
  { path: '/login', component: LoginPage },
 
  // client and admin

  { path: '/client',
    component: ClientPage, 
    children: [
      { 
        path: 'food-menu',
        component: FoodMenu
      },
      {
        path: 'order-history',
        component: OrderHistory
      },
      {
        path: 'shopping-cart',
        component: ShoppingCart
      }
    ]
  },
  { path: '/admin', component: AdminPage },
]

const router = new VueRouter({
  base: '/',
  mode: 'history',
  routes
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
