from flask import Flask,render_template
import json
app = Flask(__name__)

@app.route('/')#根目录
def how():
	return '世界你好，flask'
#url传递变量
@app.route('/key/<name>')#根目录
def key(name):
	return name
@app.route('/index')
def index():
	return render_template('index.html')

lange = ['python','java','大数据分析','易语言','c++','php','c#']
nums = [100,150,120,80,70,90,110,]

@app.route('/get_data')
def get_data():
	return json.dumps({"lange":lange,"nums":nums},ensure_ascii=False)
if __name__ == '__main__':#如果名字等于文件名
	app.run(debug=1)#开启调试模式，自动刷新
