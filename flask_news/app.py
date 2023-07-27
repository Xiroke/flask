from flask import Flask
import requests
import json

app = Flask(__name__)
counter = 0

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
	
# @app.route('/')
# @app.route('/home')
# def index():
# 	return 'Главная страница'

@app.route('/news')
def news():
	return 'Страница с новостями'

@app.route('/about')
def about():
	return 'Сайт с новостями'

@app.route('/fibonacci')
def fibonacci():
	lst = []

	for i in range(100):
		if i == 1 or i == 0:
			lst.append(1)
		else:
			lst.append(lst[i-2] + lst[i-1])

	return ' '.join(map(str, lst))

@app.route('/total/<int:a>/<int:b>')
def total(a,b):
	return f'{a + b}'





# @app.route('/money')
# def money():
# 	responce = requests.get('https://www.cbr-xml-daily.ru./daily_json.js')
# 	js = responce.json()
# 	lst = []
# 	for valute in js['Valute']:
# 		lst.append([valute['Nominal'], valute['Name'], valute['Value']])
# 	print(lst)
# 	return 'lst'

if __name__ == '__main__':
	app.run(debug=True)