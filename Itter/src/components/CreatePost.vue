<template>
  <div class="modal" :class="{ 'is-active': isActive }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-content">
      <div class="form-holder">
        <div class="form-box">
          <span class="title">Create Post</span>
          <form @submit.prevent="createPost" class="form">
            <div class="textInputWrapper">
              <label for="title">Title</label>
              <input
                v-model="title"
                placeholder="Enter title"
                type="text"
                id="title"
                name="title"
                class="textInput"
                required
              />
            </div>
            <div class="textInputWrapper">
              <label for="content">Content</label>
              <textarea
                v-model="content"
                placeholder="Enter content"
                id="content"
                name="content"
                class="textInput"
                required
              ></textarea>
            </div>
            <div class="textInputWrapper">
              <label for="tags">Tags</label>
              <input
                v-model="tags"
                placeholder="Enter tags (comma separated)"
                type="text"
                id="tags"
                name="tags"
                class="textInput"
                required
              />
            </div>
            <button class="sbutton" type="submit">Create Post</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
      title: '',
      content: '',
      tags: ''
    }
  },
  methods: {
    closeModal() {
      this.isActive = false
    },
    createPost() {
      // Call API to create post
      console.log('Creating post...')
      // ...
    }
  }
}
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  width: 500px;
}

.modal-background {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.form-holder {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.form-box {
  background-color: #252525;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  width: 400px;
}

.title {
  font-weight: bold;
  font-size: 24px;
  color: #fff;
  margin-bottom: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.textInputWrapper {
  margin-bottom: 20px;
}

.textInputWrapper label {
  font-weight: bold;
  font-size: 16px;
  color: #fff;
  margin-bottom: 10px;
}

.textInput {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #353535;
  color: #e8e8e8;
  font-size: 16px;
}

.textInput:focus {
  outline: none;
  border-color: #4caf50;
}

.sbutton {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #4caf50;
  color: #fff;
  cursor: pointer;
}

.sbutton:hover {
  background-color: #3e8e41;
}
</style>
