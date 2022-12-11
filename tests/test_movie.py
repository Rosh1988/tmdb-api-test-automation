from testhelpers import get_guest_session_id, get_api, put_api

valid_api_key = '85e760da8dc8acd92ab9b3feaae90e20'
invalid_api_key = '45sddrewfsdf8acd92ab9b3fasdsd34'

# Perform a GET request to /movie/top_rated with a valid API Key
# Check that the response status code equals 200
def test_get_top_rated_movies_check_status_code_equals_200():
    status_code, response_data = get_api('3/movie/top_rated', valid_api_key)
    assert status_code == 200


# Perform a GET request to /movie/top_rated with an invalid API Key
# Check that the response status code equals 200
# Check that the response returns a valid status_message
def test_get_top_rated_movies_check_status_code_equals_401():
    status_code, response_data = get_api('3/movie/top_rated', invalid_api_key)
    assert status_code == 401
    assert response_data['status_message'] == 'Invalid API key: You must be granted a valid key.'


# Fetch a guest_session_id
# Perform a PUT request to /movie/{movie_id}/rating with a valid API Key & guest_session_id
# Check that the response status code equals 201
# Check that the response returns a valid status_message
def test_put_rate_movie_check_status_code_equals_201():
    data='{"value": 8.5}'
    guest_id = get_guest_session_id('3/authentication/guest_session/new', valid_api_key)
    status_code, response_data = put_api('3/movie/2/rating', valid_api_key, guest_id, data)
    assert status_code == 201
    assert response_data['status_message'] == 'Success.'

# Fetch a guest_session_id
# Perform a PUT request to /movie/{movie_id}/rating with a an invalid API Key & guest_session_id
# Check that the response status code equals 401
# Check that the response returns a valid status_message
def test_put_rate_movie_check_status_code_equals_401():
    data='{"value": 8.5}'
    guest_id = get_guest_session_id('3/authentication/guest_session/new', valid_api_key)
    status_code, response_data = put_api('3/movie/2/rating', invalid_api_key, guest_id, data)
    assert status_code == 401
    assert response_data['status_message'] == 'Invalid API key: You must be granted a valid key.'
