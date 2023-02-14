<template>
  <div id="uploadfile">
    <h2>
      Upload a new file
    </h2>

    <b-form>
      <b-form-file
        v-model="file1"
        :state="Boolean(file1)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
    </b-form>

    <b-button id="uploadbutton" @click="uploadFile">Upload</b-button>
  </div>
</template>
    
<script>
export default {
  name: "UploadFile",
  data() {
    return {
      file1: null,
    }
  },
  methods: {
    uploadFile() {
      let path = `/api/${this.$route.params.username}/${this.$route.params.customer}/files/${this.file1.name}`
      let url = new URL(path, window.location)

      fetch(url, {
        method: "PUT",
        body: this.file1
      }).then(resp => {
        console.log(resp);
        this.$router.go(-1)
      })
    }
  }
}
</script>
  
<style>
#uploadfile {
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
  margin-right: 10%;
}

#uploadbutton {
  margin-top: 1%;
}
</style>
  