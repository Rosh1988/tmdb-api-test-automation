from testhelpers import get_guest_session_id, get_api, put_api
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

valid_api_key = os.getenv('valid_api_key')
invalid_api_key = os.getenv('invalid_api_key')
valid_movie_id = os.getenv('valid_movie_id')
invalid_movie_id = os.getenv('invalid_movie_id')
msg_invalid_key = os.getenv('msg_invalid_key')
msg_success = os.getenv('msg_success')
msg_not_found = os.getenv('msg_not_found')

"""
1.1 Perform a GET request to /movie/top_rated with a valid API Key
Check that the response status code equals 200
"""
def test_get_top_rated_movies_status_code_200():
    status_code, response_data = get_api('3/movie/top_rated', valid_api_key)
    assert status_code == 200

"""
1.2 Perform a GET request to /movie/top_rated with an invalid API Key
Check that the response status code equals 401
Check that the response returns a valid status_message
"""
def test_get_top_rated_movies_status_code_401():
    status_code, response_data = get_api('3/movie/top_rated', invalid_api_key)
    assert status_code == 401
    assert response_data['status_message'] == msg_invalid_key

"""
2.1 Fetch a guest_session_id
Perform a PUT request to /movie/{movie_id}/rating with a valid API Key & guest_session_id
Check that the response status code equals 201
Check that the response returns a valid status_message
"""
def test_put_rate_movie_status_code_201():
    data='{"value": 8.5}'
    guest_id = get_guest_session_id('3/authentication/guest_session/new', valid_api_key)
    status_code, response_data = put_api(f'3/movie/{valid_movie_id}/rating', valid_api_key, guest_id, data)
    assert status_code == 201
    assert response_data['status_message'] == msg_success

"""
2.2 Fetch a guest_session_id
Perform a PUT request to /movie/{movie_id}/rating with a an invalid API Key & guest_session_id
Provide an invalid API key
Provide a valid movie id
Check that the response status code equals 401
Check that the response returns a correct status_message
"""
def test_put_rate_movie_status_code_401():
    data='{"value": 8.5}'
    guest_id = get_guest_session_id('3/authentication/guest_session/new', valid_api_key)
    status_code, response_data = put_api(f'3/movie/{valid_movie_id}/rating', invalid_api_key, guest_id, data)
    assert status_code == 401
    assert response_data['status_message'] == msg_invalid_key

"""
2.3 Fetch a guest_session_id
Perform a PUT request to /movie/{movie_id}/rating
Provide invalid movie id and valid API key
Check that the response status code equals 404
Check that the response returns a correct status_message
"""
def test_put_rate_movie_status_code_404():
    data='{"value": 8.5}'
    guest_id = get_guest_session_id('3/authentication/guest_session/new', valid_api_key)
    status_code, response_data = put_api(f'3/movie/{invalid_movie_id}/rating', valid_api_key, guest_id, data)
    assert status_code == 404
    assert response_data['status_message'] == msg_not_found