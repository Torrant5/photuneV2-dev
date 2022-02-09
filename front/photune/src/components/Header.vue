<template>
  <b-carousel
    id="carousel-fade" fade no-hover-pause
    class="mb-4 shadow-sm"
  >
    <b-carousel-slide img-src="img/key_visual_trm/key_visual_7_trm.jpg"></b-carousel-slide>
    <b-carousel-slide img-src="img/key_visual_trm/key_visual_1_trm.jpg"></b-carousel-slide>
    <b-carousel-slide img-src="img/key_visual_trm/key_visual_2_trm.jpg"></b-carousel-slide>
    <b-carousel-slide img-src="img/key_visual_trm/key_visual_3_trm.jpg"></b-carousel-slide>
    <b-carousel-slide img-src="img/key_visual_trm/key_visual_5_trm.jpg"></b-carousel-slide>
    <b-carousel-slide img-src="img/key_visual_trm/key_visual_8_trm.jpg"></b-carousel-slide>
  
    <b-row class="h-100 w-100 m-0" 
    style="position: absolute; top: 0; left: 0; z-index: 5; background: rgba(255,255,255,0.4);"></b-row>
    <b-row class="h-100 w-100 m-0" align-v="center"
     style="position: absolute; top: 0; left: 0; z-index: 10;">
        <b-col cols="4">
            <img src="img/key_visual/kentrance.png" alt=""
            :class="{ 'img-pc': isPc, 'w-100': !isPc}">
        </b-col>
        <b-col cols="6" v-if="!isPc">
            <img class="w-100" src="img/key_visual/s_title.png" alt="">
        </b-col>
        <b-col cols="7" v-if="isPc">
            <img class="w-100" src="img/key_visual/pc_title.png" alt="">
        </b-col>
    </b-row>
  </b-carousel>

</template>

<script>
export default {
  name: 'Header',
  data: function () {
    return {
      width: window.innerWidth,
      height: window.innerHeight,
      isPc: true
    }
  },
  methods: {
    handleResize: function() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      if (this.width > 650){
          this.isPc = true
      }else{
          this.isPc = false
      }
    }
  },
  mounted: function () {
    this.handleResize()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy: function () {
    window.removeEventListener('resize', this.handleResize)
  }
}
</script>

<style>
.carousel-inner {
    max-height: 400px;
}

.img-pc {
    max-height: 300px;
}
</style>