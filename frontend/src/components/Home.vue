<template>
  <v-container>
    <v-row>
      <v-col
        v-for="movie in movies"
        :key="movie.id"
        cols="12" sm="6" md="3"
      >
        <v-card class="hoverable" outlined @click="goToMovie(movie.id)">
          <!-- Poster -->
          <v-img
            :src="movie.poster"
            height="350px"
            cover
          ></v-img>

          <!-- Info -->
          <v-card-text>
            <div class="movie-title">{{ movie.title }}</div>
            <div class="movie-subtitle">{{ movie.year }}, {{ movie.genre }}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      movies: []
    }
  },
  created() {
    axios.get('http://127.0.0.1:8000/api/movies/')
      .then(res => {
        this.movies = res.data
      })
  },
  methods: {
    goToMovie(id) {
      this.$router.push(`/movie/${id}`)
    }
  }
}
</script>

<style scoped>
.movie-title {
  font-weight: bold;
  font-size: 1.1rem;
  margin-top: 8px;
}
.movie-subtitle {
  color: gray;
  font-size: 0.9rem;
}
</style>
