<template>
  <div id="app">
    <div class="container">
      <!-- 1-3. 호출하시오. 
        필요한 경우 props를 데이터를 보내줍니다.
      -->
      <MovieList :movies="movies" :genres="genres"></MovieList>
    </div>
  </div>
</template>

<script>
const axios = require('axios');
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,
import MovieList from './components/movies/MovieList.vue'


export default {
  name: 'app',
  // 1-2. 아래에 등록 후
  components:{
    MovieList,
  },
  data() {
    return {
      // 활용할 데이터를 정의하시오.
      movies: [],
      genres: [],

    }
  },
  mounted() {
    // 0. mounted 되었을 때, 
    // 1) 제시된 URL로 요청을 통해 data의 movies 배열에 해당 하는 데이터를 넣으시오. 
    // 2) 제시된 URL로 요청을 통해 data의 genres 배열에 해당 하는 데이터를 넣으시오.
    // axios는 위에 호출되어 있으며, node 설치도 완료되어 있습니다.
    axios.get('https://gist.githubusercontent.com/edujustin-hphk/44fe0be46c05695fcd3efba082f90421/raw/0302e483aa3603661c1e2596587fcf07faab41c2/movie.json')
    .then(res => {
    this.movies = res.data
      

    })

    axios.get('https://gist.githubusercontent.com/edujustin-hphk/1b18def195ee03383324d43b136cee0c/raw/b24f9f5557914cdbfbeb5bdd8ed2324b36af502a/genre.json')
    .then(res => {
    this.genres = res.data

    })

  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
