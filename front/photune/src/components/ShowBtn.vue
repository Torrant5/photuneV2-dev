<template>
    <b-button variant="light" class="m-1 p-0 border border-secondary">
        <b-icon v-if="isShow" icon="arrows-angle-contract" font-scale="1" @click="onClick"></b-icon>    
        <b-icon v-if="!isShow" icon="arrows-angle-expand" font-scale="1" @click="onClick"></b-icon>    
    </b-button>
</template>

<script>
export default {
  name: 'ShowBtn',
  props: {
    msg: String,
    isShow: Boolean,
  },
  methods: {
      onClick (){
          this.$emit('click')
      }
  },
}
</script>

<style scoped>
button {
  width: 30px;
  height: 30px;
}
</style>