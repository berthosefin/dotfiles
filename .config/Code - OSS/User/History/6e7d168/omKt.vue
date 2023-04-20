<template>
  <div class="wrapper">
    <nav class="navbar is-dak">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>E-Commerce</strong></router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
