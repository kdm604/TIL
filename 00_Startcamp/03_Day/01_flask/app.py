from flask import Flask
import datetime


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'
    
@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019, 11, 29)
    td = endgame - today
    return f'SSAFY 1학기 종료까지 {td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is html h1 tag!</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄로 작성하자!</h>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """


@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!'

@app.route('/cube/<int:number>')
def mul(number):
    return f'{number}의 3제곱은 {number**3}입니다.'

# 점심 메뉴 리스트(5개)에서 2개를 뽑아 출력하기

@app.route('/lunch/<int:person>')

def select(person):
    import random

    lunch = ['피자1','피자2','피자3','피자4','피자5']
    result = random.sample(lunch,person)
    return str(result)