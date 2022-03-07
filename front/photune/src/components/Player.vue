<template>
    <b-container class="mt-4 mb-5">
        <!-- <b-row v-if="this.$store.state.playlistID"> -->
        <b-row>
            <b-col cols="12">                
                <b-card :header="init_title" header-tag="header"
                 class="shadow-sm mycard" v-if="this.$store.state.playlistID == ''">
                    Let's Post!
                </b-card>

                <b-card :header="this.$store.state.playlistName" header-tag="header"
                 class="shadow-sm mycard" v-if="this.$store.state.playlistID">
                    <iframe id="music_player" :src="playlistUrl" width="300" height="80" class="shadow-sm"
                    frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe>
                </b-card>
            </b-col>
        </b-row>
    </b-container>
</template>


<script>
export default {
    name: 'Player',
    props: {
    msg: String
    },
    data () {
        return {
            init_title : "PLAYLIST"
        }
    },
    computed: {
        playlistUrl () {
            return "https://open.spotify.com/embed/" +this.$store.state.playlistID
        }
    }
}
</script>

<style scoped>
.mycard {
    font-size: 1.5rem;
}
</style>