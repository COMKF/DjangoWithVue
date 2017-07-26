<template>
  <div class="">
    <h1>{{ msg }}</h1>
    <h2>{{ msg2 }}</h2>
    <button v-on:click="onClickMe">Click!!!</button>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        msg: 'hello , mk'
      }
    },
    props: ['msg2'], // 这里演示父组件向子组件传递数据，用msg演示。子组件必须用props接收这个msg。换个思路，这也相当于声明变量。然后使用变量。
    methods: {
      onClickMe: function () {
        // 用 Click 方法，演示子组件向父组件传递数据。
        // 点击Click，通过$emit方法，第一个参数是键（通过键获取值，对应的值是一个方法），第二个参数的作用是传递参数，向对应的值（方法）传递参数。
        // 然后，父组件对应的方法就开始执行了。
        this.$emit('childXXX', 'font-size')
      }
    }
  }
</script>

<style scoped>
  .font-size { /* style只能在当前组件中使用*/
    font-size: 40px;
  }

  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
