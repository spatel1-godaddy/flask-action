from nose.tools import assert_equal
from main import app

app.config['TESTING'] = True
web = app.test_client()


def test_index():

    with app.test_request_context('/'):
        assert_equal(web.get('/').status_code, 200)
        assert_equal(web.get('/').data, b'Hello, World!')
