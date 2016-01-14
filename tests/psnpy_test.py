import requests
import json

def test_psnpy_response():
    r = requests.get("http://localhost:8000")
    message = {'message': 'Hello, world!'}
    assert r.status_code == 200
    assert r.text == json.dumps(message)
