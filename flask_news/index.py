from flask import Flask, render_template
import datetime
from news import news as news_info
app = Flask(__name__)

@app.route('/')
def index():

	context = {
		'title': 'Новостной сайт',
		'text': 'Скоро будут новости!'
	}
	
	return render_template('index.html', **context)
	

@app.route('/news')
def news():
	return 'Новости'

@app.route('/news_detail/<int:id>')
def news_detail(id):
	return render_template('news_detail.html', **news_info[id])


@app.route('/category/<string:name>')
def category(name):
	return f'{name}'

@app.route('/<string:info>')
def date(info):
	now = datetime.datetime.now()
	if info == 'date':
		return now.strftime('%d.%m.%Y')

	if info == 'time':
		return now.strftime('%H.%M')

@app.route('/<int:a>/<string:operation>/<int:b>')
def calc(a, b, operation):
	if operation == ':':
		operation == '/'
	try:
		num = eval(f'{str(a)} {operation} {str(b)}')
		return str(num)
	except:
		return 'Ошибка'

if __name__ == '__main__':
	app.run(debug=True)