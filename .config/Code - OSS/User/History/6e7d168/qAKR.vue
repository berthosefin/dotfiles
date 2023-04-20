<template>
  <div class="wrapper">
    <nav class="navbar is-dak">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>E-Commerce</strong></router-link>
        <a href="" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
        </a>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
