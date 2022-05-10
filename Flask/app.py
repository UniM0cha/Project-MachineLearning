from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# 파이썬 명령어로 실행할 수 있음
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)