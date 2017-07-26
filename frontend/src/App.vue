<template>
  <div id="p">
    <!-- 这个id只用于加载CSS -->
    <router-view></router-view>
    <!-- 路由设置，从路由加载view。查找与当前url相同的js并加载。 -->
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#p {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
