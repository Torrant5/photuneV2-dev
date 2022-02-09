import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(Vuex)
Vue.use(VueAxios, axios)

const url = process.env.VUE_APP_API_BASE
 
async function postImage (formData) {
    var uri = url + 'api/predict'
    // console.log(uri)
    const res = await axios.post(uri, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).catch(err =>{
        console.log("error")
        return err.response
    })
    return res.data
}

async function getRandom () {
    var uri = url + 'api/random'
    // console.log(uri)
    const res = await axios.get(uri)
    .catch(err =>{
        console.log("error")
        return err.response
    })
    return res.data
}

async function getSample (sampleId) {
    var uri = url + 'api/sample?id=' + String(sampleId)
    // console.log(uri)
    // console.log(sampleId)
    const res = await axios.get(uri)
    .catch(err =>{
        console.log("error")
        return err.response
    })
    return res.data
}


const store = new Vuex.Store({
    state: {
        playlistID: "",
        playlistName: ""
    },

    mutations: {
        setPlaylist (state, {ID, Name}){
            console.log(ID, Name)
            state.playlistID = "playlist/"+ID
            state.playlistName = Name
        }
    },
    actions: {
        setPlaylistImageAsync ({commit}, formData){
            return postImage(formData)
                .then( data => {
                    // console.log(data.playlist_id)
                    // console.log(data.playlist_name)
                    commit("setPlaylist", {
                        ID: data.playlist_id,
                        Name: data.playlist_name
                    })
                })
        },
        setPlaylistRandomAsync ({commit}){
            return getRandom()
                .then( data => {
                    // console.log(data.playlist_id)
                    // console.log(data.playlist_name)
                    commit("setPlaylist", {
                        ID: data.playlist_id,
                        Name: data.playlist_name
                    })
                })
        },
        setPlaylistSampleAsync ({commit}, sampleId){
            return getSample(sampleId)
                .then( data => {
                    // console.log(data.playlist_id)
                    // console.log(data.playlist_name)
                    commit("setPlaylist", {
                        ID: data.playlist_id,
                        Name: data.playlist_name
                    })
                })
        }
    }
})

export default store