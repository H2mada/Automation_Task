import requests
import json
import pytest

def test_api():

    url = 'http://api.zippopotam.us/de/bw/stuttgart'
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.get(url)       
    
    #  Verify that the response status code is 200
    assert 200 == resp.status_code

    #  And content type is JSON.
    assert "application/json" in resp.headers["Content-Type"]

    #  Verify that the response time is below 1s.
    assert 1 >= resp.elapsed.total_seconds()

    json_data  = json.loads(resp.text)

    #  Verify in Response - That "country" is "Germany" 
    assert 'Germany' == json_data['country']

    #  and "state" is "Baden-Württemberg".
    assert 'Baden-Württemberg' == json_data['state']

    #  Verify in Response - For Post Code "70597" the place name has "Stuttgart Degerloch".
    assert 'Stuttgart Degerloch' in [place['place name'] for place in json_data['places'] if place['post code'] == '70597']
    