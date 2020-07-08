<template>
  <v-app>
    <v-app-bar
      app
      dark
    >
      <div class="d-flex align-center">
        <h2>
        <v-icon size="35">
          library_add_check
        </v-icon>
          To do app
        </h2>
      </div>

      <v-spacer></v-spacer>

      <v-switch
        v-model="$vuetify.theme.dark"
        hide-details
        inset
        color="success"
      ></v-switch>

      <v-btn
        href="https://github.com/lucasfrancaid/Todo"
        target="_blank"
        text
      >
        <span class="mr-2 git-title">My Github </span>
        <v-img 
          src="./assets/github.png"
          width="40"
        />
      </v-btn>
    </v-app-bar>

    <v-main>
      <div class="d-flex align-center justify-center mt-10 mb-0">
        <h1>
        <v-icon size="50" class="success--text">
          library_add_check
        </v-icon>

          To Do List
        </h1>
      </div>
      <Todo/>
    </v-main>
  </v-app>
</template>

<script>
  import Todo from './components/Todo';

  export default {
    name: 'App',
    data: () => ({}),
    components: {
      Todo,
    },
  };
</script>

<style scoped>
v-app-bar {
  width: 100%;
  color: #2d2e2f;
}

@media screen and (max-width: 600px) {
  .git-title {
    display: none;
  }
}
</style>