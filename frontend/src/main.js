import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import Home from './components/Home.vue'
import Error from './components/NotFound.vue'
import Employee from './components/Employee.vue'
import AddEmployee from './components/AddEmployee.vue'
import Salary from './components/Salary.vue'
import titleMixin from './mixins/titleMixin'

Vue.use(Router)
Vue.mixin(titleMixin)

const router = new Router({
 mode: 'history',
 routes: [
   {
     path: '/',
     name:'home',
     meta:{title:'Сотрудники'},
     component: Home,
   },
   {
     path: '/add',
     name:'add',
     meta:{title:'Новый сотрудник'},
     component: AddEmployee,
   },
   {
     path: '/employee/:id',
     name:'employee',
     meta:{title:'Сотрудник'},
     component: Employee,
     props: true,
   },
   {
     path: '/salary/:id',
     name:'salary',
     meta:{title:'Зарплаты'},
     component: Salary,
     props: true,
   },
   {
     path: '*',
     name:'NotFound',
     component: Error,
   },
 ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
