import webbrowser

#webbrowser.open('https://google.com')
#webbrowser.open_new('https://www.naver.com')

idols = [ 'bts', 'winner', 'iu', 'red velvet']

for idol in idols:
    print(idol)
    webbrowser.open('https://search.naver.com/search.naver?query='+idol)