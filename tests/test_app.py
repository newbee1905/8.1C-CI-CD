import app

def test_hello():
	client = app.app.test_client()
	resp = client.get('/')
	assert resp.data == b'Hello, world!'

def test_echo():
	client = app.app.test_client()
	resp = client.get('/echo/foobar')
	assert b'foobar' in resp.data

def test_mul():
	client = app.app.test_client()
	resp = client.get('/mul/3/4')
	assert b'3' in resp.data and b'4' in resp.data and b'12' in resp.data
