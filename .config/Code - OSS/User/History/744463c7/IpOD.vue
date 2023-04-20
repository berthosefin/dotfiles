<template>
  <section class="todoapp">
      <header class="header">
          <h1>Todos</h1>
          <input type="text" class="new-todo" placeholder="Ajouter une tache" v-model="newTodo">
      </header>
      <div class="main">
          <ul class="todo-list">
              <li class="todo">
                  <div class="view">
                      <label>
                          Tache
                      </label>
                  </div>
              </li>
          </ul>
      </div>
  </section>
</template>

<script>

export default {
  data () {
    return {
        todos: [],
        newTodo: ''
    }
  }
}

</script>

<style src="./todos.css"></style>
