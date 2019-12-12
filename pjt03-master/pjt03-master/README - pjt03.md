# pjt03

```

/* header */
header {
  /* 상단에 고정시키며(sticky) 다른 영역보다 우선하여 볼 수 있도록 작성하세요. */
  position:fixed;
  top:0;
}

/* nav */
nav {
  /* navigation 항목을 오른쪽으로 정렬 시키세요.*/
  float: right;
}

.nav-items > li {
  /* navigation 항목을 한 줄로 만들어 주세요. */

  display: inline-block;
  

  /* 좌우 여백을 지정하세요. */

  margin-left: 5px;
  margin-right: 5px;

  /* li 태그의 bullet point를 제거 해주세요. */
  
    list-style: none;

}

.nav-items > li > a {
  /* a tag는 링크를 나타내며, 기본적으로 글자 색상이 파란색입니다. 원하는 색상으로 바꿔보세요. */
    color:red;
}

.nav-items > li > a:hover {
  /* hover는 마우스 오버시 모습입니다. 
  이때 하이라이트 되도록 다른 색상으로 바꿔보세요. */
    color: purple;
  /* a tag를 마우스 오버하면 밑줄이 나타납니다.
  text를 꾸며주고 있는 밑줄을 없애보세요. */
  text-decoration-line: none;

}

/* title section */
#section-title {
  /* 배경 이미지를 적용 해보세요. (이미지는 images/background.jpg) */
    background-image:url(images/background.jpg);
  
  /* 텍스트를 가운데 정렬 해보세요. */
    text-align: center;
  /* 텍스트를 수직 가운데 정렬 해보세요. (section-title은 높이가 300px) */
    line-height: 300px;
  

}

.section-title-heading {
  /* font size를 적절하게 조정 해주세요. (h1 기본 2rem) */
  font-size: 3rem;

}

/* aside */
aside {
  /* aside를 부모인 div#content의 영역에 위치시키세요.
  div#content는 position: relative 입니다.
  */

  /* bottom: 0; */
  position: absolute;
  top:0;
}

.aside-items {
  /* ul 태그의 자동으로 적용된 padding을 제거 해주세요. */
  padding : 0;
}

.aside-items > li {
  /* li 태그의 bullet point를 제거 해주세요. */
  list-style: none;
}

/* footer */
footer {
  /* footer는 항상 바닥에 위치하도록 position을 설정 해주세요. */
    position: fixed;
    bottom:0;

  /* 텍스트를 가운데 정렬 해주세요. */
    text-align: center;

  /* 텍스트가 수직정렬 되도록 해주세요. (footer는 높이가 50px) */
  line-height: 34px;
}

레이아웃.css에서 스타일링을 해서 index.html에 적용시키는 프로젝트를 간단하게 해보았습니다.

휑했던 실습파일을 css를 통해 그래도 봐줄만하게 꾸미면서 사용법을 더 익히게 되었습니다.
```





![](C:\Users\student\project\pjt03\project_03\결과물.jpg)