import flask
from c_extension import multiplier

app = flask.Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, world!'

@app.route('/echo/<msg>')
def echo(msg):
	# insecure: reflects user input without sanitisation
	return f'You said: {msg}'

@app.route('/mul/<int:a>/<int:b>')
def mul(a, b):
	result = multiplier(a, b)
	return f'{a} × {b} = {result}'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

