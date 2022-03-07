<template>
  <div id="app" class="m-0">

    <Navbar />

    <Header style="margin-top: -48px;" />

    <b-container class="p-0">
      <b-row align-h="center">
        <b-col cols="12">
          <How />
        </b-col>
        <b-col cols="12" lg="7">
          <PostForm />
        </b-col>
        <b-col cols="12" lg="5">
          <Player /> 
        </b-col>
      </b-row>
    </b-container>

    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Header from './components/Header.vue'
import How from './components/How.vue'
import PostForm from './components/PostForm.vue'
import Player from './components/Player.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Header,
    How,
    PostForm,
    Player,
    Footer
  }
}
</script>

<style>
@charset "UTF-8";
@import url("https://fonts.googleapis.com/css2?family=Kosugi&family=Montserrat&display=swap");

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

  background: #f9f9f9;
  font-family: 'Kosugi', sans-serif;
  font-family: 'Montserrat', sans-serif;
}
</style>
