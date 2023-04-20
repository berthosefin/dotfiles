<template>
  <div class="wrapper">
    <nav class="navbar is-dak">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>E-Commerce</strong></router-link>
        <a href="" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link to='/summer' class="navbar-item">Summer</router-link>
          <router-link to='/winter' class="navbar-item">Winter</router-link>

          <div class="navbar-item">
            <div class="button">
              <router-link to='/log-in' class="button is-light">Log In</router-link>
              <router-link to='/cart' class="button is-success">
                <span class="icon"><i class="fas fa shopping-cart"></i></span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
