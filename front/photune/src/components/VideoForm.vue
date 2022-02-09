<template>
    <b-overlay :show="isProcessing" rounded="sm" spinner-variant="primary">
        <b-col cols="12" class="d-flex flex-row-reverse position-absolute">
            <ShowBtn :isShow="isShow" v-on:click="isShow = !isShow" class="position-relative"/>
        </b-col>
        <b-container>
            <b-row v-show="isShow" align-h="center">
                <b-col cols="12">
                    <b-button variant="outline-primary" @click="mountCamera" v-if="!isCameraOn">Camera ON</b-button>
                    <b-overlay :show="isStartingUp" 
                        rounded="sm" spinner-variant="secondary">
                        <video ref="video" id="video" class="w-75 shadow-sm" autoplay v-show="isCameraOn"></video>
                    </b-overlay>
                </b-col>
                <b-col cols="12" class="my-2">
                    <b-row align-h="center">
                        <b-col cols="4">
                            <b-button variant="secondary" @click="capture()" id="snap"
                            :disabled="!isCameraOn" class="w-100 shadow-sm">Snap!!</b-button>
                        </b-col>
                        <b-col cols="2"></b-col>
                        <b-col cols="4">
                            <b-button variant="primary" @click="postSnap"
                            :disabled="url === ''" 
                            class="w-100 shadow-sm">Post!</b-button>
                        </b-col>
                    </b-row>
                </b-col>
                <b-col cols="10" class="my-2">
                    <b-input-group prepend="interval (min)" class="shadow-sm">
                        <b-form-input type="number" v-model="interval" @change="stop"
                         min="1"></b-form-input>
                        <b-button @click="start" v-if="!isTimerOn" variant="primary"
                         :disabled="!isCameraOn">Auto Snap&Post Start</b-button>
                        <b-button @click="stop" v-if="isTimerOn" variant="danger"
                         :disabled="!isCameraOn">Auto Snap&Post Stop</b-button>
                    </b-input-group>
                </b-col>
                <canvas ref="canvas" id="canvas" class="d-none"></canvas>
                <b-col cols="12" class="my-2">
                    <div v-if="url">
                        <img :src="url" class="w-50 shadow-sm">
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </b-overlay>
</template>

<script>
import ShowBtn from './ShowBtn.vue'

export default {
    name: 'VideoForm',
    props: {
        msg: String
    },
    components: {
        ShowBtn
    },
    data() {
        return {
            url:"",
            brob: null,
            isShow: true,
            isCameraOn: false,
            isStartingUp: false,
            isProcessing: false,
            isTimerOn: false,
            interval: 5,
            video: {},
            canvas: {},
            timer: null
        }
    },
    computed: {
        showBtnMsg: function () {
            return this.isShow ? "非表示" : "表示"
        },

    },
    methods: {
        mountCamera (){
            this.isCameraOn = true
            this.isStartingUp = true
            this.video = this.$refs.video
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
                this.video.srcObject = stream
                this.video.play()
                this.isStartingUp = false
                })
            }
        },
        capture () {
            this.canvas = this.$refs.canvas
            this.canvas.width = this.video.videoWidth
            this.canvas.height = this.video.videoHeight
            this.canvas.getContext('2d').drawImage(this.video, 0, 0)
            this.url = this.canvas.toDataURL('image/png')
            this.brob = new Promise(resolve => this.canvas.toBlob(resolve, 'image/png'))
        },
        start () {
            this.capture()
            this.postSnap()
            this.timer = setInterval(()=>{
                this.capture()
                this.postSnap()
            }, this.interval*60*1000)
            this.isTimerOn = true
        },
        stop (){
            clearInterval(this.timer)
            this.isTimerOn = false
        },
        async postSnap (){
            this.isProcessing = true
            var formData = new FormData()
            formData.append("file", await this.brob, "image.png")

            await this.$store.dispatch('setPlaylistImageAsync', formData)
            this.isProcessing = false
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