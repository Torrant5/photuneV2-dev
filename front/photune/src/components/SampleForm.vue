<template>
    <b-overlay :show="isProcessing" rounded="sm" spinner-variant="primary">
        <b-col cols="12" class="d-flex flex-row-reverse position-absolute">
            <ShowBtn :isShow="isShow" v-on:click="isShow = !isShow" class="position-relative"/>
        </b-col>
        <b-container>
            <b-row v-show="isShow">
                <b-col cols="12">
                    <b-tabs content-class="m-3" variant="secondary" 
                      pills justified :vertical="isVertical" :end="!isVertical"
                      active-nav-item-class="bg-secondary text-white shadow-sm">
                        <b-tab title="Sample 1" :title-link-class="'text-secondary'" @click="sampleClick(1)" active>
                            <img src="img/key_visual_trm/key_visual_7_trm.jpg" alt="" class="w-100 shadow-sm">
                        </b-tab>
                        <b-tab title="Sample 2" :title-link-class="'text-secondary'" @click="sampleClick(2)">
                            <img src="img/key_visual_trm/key_visual_5_trm.jpg" alt="" class="w-100 shadow-sm"></b-tab>
                        <b-tab title="Sample 3" :title-link-class="'text-secondary'" @click="sampleClick(3)">
                            <img src="img/key_visual_trm/key_visual_3_trm.jpg" alt="" class="w-100 shadow-sm"></b-tab>
                    </b-tabs>
                </b-col>
                <b-col cols="12" class="my-2">
                    <b-row align-h="center" align-v="center">
                        <b-col cols="5" sm="4">
                            <b-button variant="outline-primary" @click="getRandom"
                             class="w-100 shadow-sm">Random!</b-button>
                        </b-col>
                        <b-col cols="1" sm="2"></b-col>
                        <b-col cols="5" sm="4">
                            <b-button variant="primary" @click="getSample"
                             class="w-100 shadow-sm">Post!</b-button>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
        </b-container>
    </b-overlay>
</template>

<script>
import ShowBtn from './ShowBtn.vue'

export default {
    name: 'SampleForm',
    props: {
    msg: String
    },
    components: {
        ShowBtn
    },
    data() {
        return {
            isShow: true,
            isProcessing: false,
            isVertical: true,
            sampleId: 1,
        }
    },
    computed: {
        showBtnMsg: function () {
            return this.isShow ? "非表示" : "表示"
        },

    },
    mounted: function () {
        if (window.innerWidth < 450){
            this.isVertical = false
        }
    },
    methods: {
        async getRandom (){
            this.isProcessing = true
            await this.$store.dispatch('setPlaylistRandomAsync')
            this.isProcessing = false
        },
        async getSample (){
            this.isProcessing = true
            await this.$store.dispatch('setPlaylistSampleAsync', this.sampleId)
            this.isProcessing = false
        },
        sampleClick (idx) {
            this.sampleId = idx
        }

    },
}
</script>


<style scoped>
.container {
    padding-top: 19px;
    padding-bottom: 19px;
}
</style>
