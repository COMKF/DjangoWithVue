// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'  // 省略了vue后缀，全名是./App.vue
// 这个import语法跟java，python都不同。相当于 var APP = require（'./App'）
import router from './router/index'

Vue.config.productionTip = false

// mian.js的意义是配置全局的属性
/* eslint-disable no-new */
new Vue({
  el: '#a', // el就是名称，html根据el的值进行匹配，然后加载。
  router,   // 这个router属性名必须固定，路由配置，以后都会从./vms这个文件夹下加载资源
  // mian.js中必须有template和components属性。
  template: '<App/>',  // Html中显示的名称，必须与载入的vue同名。全局配置，必须有这个属性。
  components: {App}   // 进行注册，注册了才能使用。载入App.vue。全局配置，必须有这个属性。
})
