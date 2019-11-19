# PJT09 - README

1. ## App.vue

   - 컴포넌트를 불러오기 위해 3단계의 작업을 실시(Import , components 추가, 호출)
   - axios를 이용하여 JSON 파일을 app.data에 저장 ( movies, genres)

2. ## MovieList

   - MovieListitem을 받기 위해서 컴포넌트를 불러옴.

   - props설정을 통해 상위 컴포넌트 (App) 으로부터 Array를 받아서 사용함

   - 받아온 데이터를 분기 시키기 위해서 App에서 받아온 movies를 담을 새로운 배열을 selectm 으로 선언.

   - genreId의 값을 받기 위해서 v-model로 DOM과 Vue를 연결시켜 그 값에 따른 movies 분기를 함

     1) Methods 활용.

     ​	select tag에 @click으로 methods를 사용하면 그 값이 변화할때 그 함수를 실행 시킬 수 있어서 선택 할 때마다 함수를 실행 시킴.

     2) watch 활용

     ​	watch를 사용하게 되면 Vue 인스턴스안에 있는 변수값이 변화할때 함수를 실행하게 됨.

     둘다 genreId를 활용하여서 상위 컴포넌트로부터 받아온 movies는 손상시키지 않으면서 selectm에 filter를 사용하여 원하는 정보를 담아서 화면에 출력.

   - selectedGenreId의 default 값을 0으로 지정해주면 새로고침시에도 선택창이 비어있지 않게 됨

3. ## MovieListitem

   - props설정으로 Array를 받는 것이 아니라 하나의 특정 Object를 받아서 그 Object의 이미지, 제목 출력함.
   - Modal를 활용하기 위해 button 태그의 v-bind:data-target를 활용하여 동적으로 값을 할당 할 수 있음.

4. ## MovieListitemModal

   - modal의 id를 설정.
   - data를 활용하지는 않지만 Object를 리턴해줘야 watch를 사용할때 제대로 작동을 하게 됨.

    

5. ## 느낀 점

   - 웹 공부를 많이 해야겠다고 느꼈네요.
   - 비동기식 처리를 이용하여 웹페이지를 구현하니 이전에 Django로써는 이해되지않는 오류들이 발생하고, 이를 처리하는 방법을 통하여 SAP의 대한 이해가 깊어짐.
   - SAP가 복잡해지면 더욱 어려워 질 것 같음.
   - 기능별로 컴포넌트 파일이 나눠져있기 때문에 협업하기에 좋은 툴 인 거 같습니다.