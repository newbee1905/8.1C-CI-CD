import app

def test_hello():
	client = app.app.test_client()
	resp = client.get('/')
	assert resp.data == b'Hello, world!'

def test_echo():
	client = app.app.test_client()
	resp = client.get('/echo/foobar')
	assert b'foobar' in resp.data

