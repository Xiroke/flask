from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def index():
	return '''
	<!DOCTYPE html>
	<html>
	      <head>      
	         <meta charset="utf-8">         
	         <title>Моя HTML страница</title>      
	      </head>   
	      <body>      
	         <h1>Привет, мир!</h1>         
	         <p>Я создал эту страницу с помощью Flask.</p>         
	      </body>
	</html>
	'''

@app.route('/news')
def news():
	return 'Новости'

@app.route('/news_detail/<int:id>')
def news_detail1(id):
	return f'Новость {id}'

@app.route('/news_detail/<int:id>')
def news_detail2():
	return f'Новость {id}'

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