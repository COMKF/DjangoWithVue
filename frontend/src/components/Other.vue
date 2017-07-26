<template>
  <div>
    <h1>{{ title }}</h1>
    <h1 v-text="title"></h1>
    <h1 v-html="title"></h1>
    <input type="password" v-model="newItem" @keyup.enter="addNew()">
    <!-- 每当键盘敲击enter的时候，就触发事件addNew -->
    <ul>
      <!--<li v-for="item in itemsss" class="finished">--> <!-- 最开始的做法 -->
      <!--<li v-for="item in itemsss" v-bind:class="{finished: item.isFinished}">-->
      <!-- 用v-bind绑定class，并使用isFinished进行控制是否使用该class -->
      <li v-for="i in itemsss" :class="[{finished: i.isFinished},childWords]" class="red" v-on:click.once="toggleFinish(i)">
        <!-- 用v-bind绑定class，可以简写为:class= -->
        <!-- 用v-on绑定click事件 -->
        {{ i.label }}
      </li>
    </ul>
    <!--<com-a msg2="what to do"></com-a> -->
    <!--在模板上渲染和使用comA，命名必须是com-a，因为vue会处理comA，把大写变小写，并在前面加个- -->
    <!-- 这里演示父组件向子组件传递数据，用msg演示 -->

    <com-a :msg2="title" v-on:childXXX="listenfromchild"></com-a>
    <!-- 这里演示子组件向父组件传递数据，用v-on演示，向子组件绑定一个键值对，键为'child'，值为一个方法'listenfromchild' -->
    <template>
      <!--支持template间接嵌套，也就是说支持 template - div（或其他元素） - template，不支持template直接嵌套-->
      <p>from child:{{ childWords }}</p>
    </template>
  </div>
</template>

<script>
  import comA from './comA' // 引入其他的vue

  import Store from './store' // 引入其他的js，以及其函数功能
  console.log(Store)
  export default {
    data: function () { // 数据写在data里，也可以直接写成 data ()
      return {
        title: '<p>this is a todo list</p>',
        itemsss: Store.fetch(),
        newItem: '',
        childWords: '' // 要在页面上使用childWords，必须先进行定义。
      }
    },
    methods: {  // 用到的方法写在methods里
      toggleFinish: function (item) {
        item.isFinished = !item.isFinished
      },
      addNew: function () {
        this.itemsss.push({  // 添加itemsss数据
          label: this.newItem,
          isFinished: false
        })
        this.newItem = ''
      },
      listenfromchild: function (Words) {
        this.childWords = Words
      }
    },
    watch: {  // watch，相当于监听。
      itemsss: { // 首先是需要监听的对象
        handler: function (item) { // 然后是需要调用的回调函数。这里的回调函数是 操作各种选项。除此之外，回调函数还可以是自定义的方法，或者方法名。
          Store.save(item)
        },
        deep: true // handler和deep都是已经定义好的选项，每个选项有自己的功能。handler的功能不明，用了再说。
        // deep的功能是深度监听。当对象内的值变化时，deep为true时，会监听这些变化，为false时，不会监听这些变化。
      }
    },
    components: {comA}, // 引入其他的vue，需要注册
    events: {}
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .font-size{ /* style只能在当前组件中使用*/
    font-size: 40px;
  }

  .red{
    color: red;
  }
  .finished {
    text-decoration: underline;
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
