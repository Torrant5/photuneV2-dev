<template>
    <b-container class="my-4">
      <b-row>
        <b-col cols="12">
          <b-card no-body class="shadow-sm">
            <b-tabs justified card>
              <b-tab title="Photo" active no-body>
                <b-card-text><PhotoForm /></b-card-text> 
              </b-tab>
              <b-tab title="Video" no-body>              
                <b-card-text><VideoForm /></b-card-text>
              </b-tab>
              <b-tab title="Sample" no-body>              
                <b-card-text><SampleForm /></b-card-text>
              </b-tab>
            </b-tabs>
          </b-card> 
        </b-col>
      </b-row>
    </b-container>
</template>


<script>
import PhotoForm from './PhotoForm.vue'
import VideoForm from './VideoForm.vue'
import SampleForm from './SampleForm.vue'

export default {
  name: 'PostForm',
  props: {
    msg: String
  },
  components: {
    PhotoForm,
    VideoForm,
    SampleForm
  }
}
</script>