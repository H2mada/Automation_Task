import requests
import json
import pytest

@pytest.mark.parametrize('data' , [
        {'country':'us', 'post code':'90210', 'place name': 'Beverly Hills'},
        {'country':'us', 'post code':'12345', 'place name': 'Schenectady'},
        {'country':'ca', 'post code':'B2R', 'place name': 'Waverley'}])
def test_api_data_driven(data):

    url = 'http://api.zippopotam.us/{}/{}'.format(data['country'],data['post code'])
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.get(url)       
    
    #  Verify that the response status code is 200
    assert 200 == resp.status_code

    #  And content type is JSON.
    assert "application/json" in resp.headers["Content-Type"]

    #  Verify that the response time is below 1s.
    assert 1 >= resp.elapsed.total_seconds()

    json_data  = json.loads(resp.text)

    #  Verify in Response - "Place Name" for each input "Country" and "Postal Code"
    assert data['place name'] in [place['place name'] for place in json_data['places']]