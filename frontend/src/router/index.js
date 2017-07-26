import Vue from 'vue'
import Router from 'vue-router'
import Hello from '../components/Hello.vue'
import Other from '../components/Other.vue'

Vue.use(Router)
// 加载路由，使这个js可以从路由进行查找

export default new Router({
  routes: [
    {
      path: '/12', // 当路由（url）为/时，加载这个js。
      // name: 'Hello', // 这个属性可以舍去。
      component: Hello  // 载入Hello.vue。
    },
    {
      path: '/34', // 当路由（url）为/时，加载这个js。
      // name: 'Hello', // 这个属性可以舍去。
      component: Other  // 进行注册，注册了才能使用。载入Other.vue。
    }
  ]
})
