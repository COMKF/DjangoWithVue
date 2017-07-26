/**
 * Created by yemenghao on 2017/7/13.
 */
const STORAGE_KEY = 'todos-vuejs'
export default {
  fetch () {
    return JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '[]')
  },
  save (items) {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(items))
  }
}
// 该js的功能是刷新页面时，保存上一次在本页面上的操作。原理是把数据保存在window.localStorage里，每次刷新，从window.localStorage调出数据。
