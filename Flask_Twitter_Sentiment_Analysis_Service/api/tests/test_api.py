import pytest
import requests
from api import create_app
from flask import url_for

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_index_page():
    r = requests.get(url+'/') # Assumses that it has a path of "/"
    assert r.status_code == 200 # Assumes that it will return a 200 response

def test_tweets_list():
    r = requests.get(url+'/api/get/tweets/all') # Assumses that it has a path of "/"
    assert r.status_code == 200 # Assumes that it will return a 200 response

def test_prediction():
    r = requests.get(url+'/api/get/tweets/prediction') # Assumses that it has a path of "/"
    assert r.status_code == 200 # Assumes that it will return a 200 response

def test_tweets_statistics():
    r = requests.get(url+'/api/get/tweets/statistics') # Assumses that it has a path of "/"
    assert r.status_code == 200 # Assumes that it will return a 200 response