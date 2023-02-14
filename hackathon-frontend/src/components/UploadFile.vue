<template>
  <div id="uploadfile">
    <h2>
      Upload a new file
    </h2>

    <b-form-file
      v-model="file1"
      :state="Boolean(file1)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    />
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
    uploadFile() {}
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
</style>
  