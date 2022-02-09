<template>
    <b-col cols="12" md="2" class="member mx-auto my-3">
        <b-row align-h="center">
            <b-col cols="3" md="12" class="p-0 my-auto">
                <img :src="'img/icon/'+filename" alt=""
                class="w-100 rounded-circle">
            </b-col>
            <b-col cols="9" md="12" class="my-auto py-2">
                <b-row class="desc">
                    <b-col cols="12" class="h4">{{name}}</b-col>
                    <b-col cols="12">{{univ}}</b-col>
                    <b-col cols="12">{{msg}}</b-col>
                </b-row>         
            </b-col>
        </b-row>
    </b-col>
        
</template>

<script>
export default {
  name: 'Member',
  props: {
      name: String,
      univ: String,
      msg: String,
      filename: String,
  }
}
</script>

<style scoped>
.member {
    font-size: 12px;
    font-weight: none; 
    /* text-align:center; */
}

.member img {
    max-width: 150px;
}

.desc {
    text-align: left;
}

h1 {
    font-size: 20px;
    font-weight: bold;
    color: #f9f9f9;
}
</style>