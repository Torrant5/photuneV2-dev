<template>
    <b-overlay :show="isProcessing" rounded="sm" spinner-variant="primary">
        <b-col cols="12" class="d-flex flex-row-reverse position-absolute">
            <ShowBtn :isShow="isShow" v-on:click="isShow = !isShow" class="position-relative"/>
        </b-col>
        <b-container class="px-0">
            <b-row v-show="isShow" align-h="center">
                <b-col cols="12" sm="4" align-self="center">
                    <label type="button" class="btn btn-secondary p-2 m-2 shadow-sm w-75">
                        <b-icon icon="camera"></b-icon>
                        CHOOSE!
                        <input id="photo-input" type="file" ref="preview" 
                            @change="uploadFile" class="d-none">
                    </label>
                    <b-button variant="primary" @click="postPhoto" 
                        :disabled="url===''" class="m-2 p-2 shadow-sm w-75">Post!</b-button>
                </b-col>
                <b-col cols="10" sm="6" align-self="center" v-if="url!==''">
                    <div v-if="url" class="m-2">
                        <img :src="url" class="w-100 shadow-sm">
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </b-overlay>
</template>

<script>
import ShowBtn from './ShowBtn.vue'

export default {
    name: 'PhotoForm',
    props: {
    msg: String
    },
    components: {
        ShowBtn
    },
    data() {
        return {
            url:"",
            isShow: true,
            isProcessing: false,
        }
    },
    computed: {
        showBtnMsg: function () {
            return this.isShow ? "非表示" : "表示"
        },

    },
    methods: {
        uploadFile (){
            const file = this.$refs.preview.files[0];
            this.url = URL.createObjectURL(file)
        },
        async postPhoto (){
            this.isProcessing = true
            var formData = new FormData()
            var file = document.getElementById("photo-input")
            formData.append('file', file.files[0])
            console.log(file.files[0])

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