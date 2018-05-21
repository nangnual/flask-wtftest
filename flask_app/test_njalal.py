from flask_app.app_aggregator import create_app

import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    client = app.test_client()

    yield client

def test_conn(client):
    rv = client.get('/blog/create')

    assert b'are we there yet?' in rv.data