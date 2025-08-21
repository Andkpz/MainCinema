<template>
  <v-container v-if="movie">
    <v-row>
      <!-- Poster -->
      <v-col cols="12" md="4">
        <v-img :src="movie.poster" aspect-ratio="2/3" contain></v-img>
      </v-col>

      <!-- Info -->
      <v-col cols="12" md="8">
        <h1>{{ movie.title }}</h1>
        <p>{{ movie.genre }}</p>
        <p>{{ movie.year }}</p>
        <p>{{ movie.duration }} min</p>
        <v-divider class="my-2"></v-divider>
        <p>{{ movie.description }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      movie: null
    }
  },
  created() {
    const id = this.$route.params.id
    axios.get(`http://127.0.0.1:8000/api/movies/${id}/`)
      .then(res => {
        this.movie = res.data
      })
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 10px;
}
</style>
