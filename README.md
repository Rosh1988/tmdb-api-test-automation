<h1 align="center">TMDB API Test Automation</h1>

This project automates the API testing for https://www.themoviedb.org/

Following endpoints are in scope for the automation:

- GET /movie/top_rated : [Get the top rated movies on TMDB](https://developers.themoviedb.org/3/movies/get-top-rated-movies "Get the top rated movies on TMDB")
- POST /movie/{movie_id}/rating: [Rate a movie on TMDB](https://developers.themoviedb.org/3/movies/rate-movie "Rate a movie on TMDB")

> Note: Load testing framework using locust is implemented for the endpoint GET /movie/top_rated only.

## Dependencies

* __Python__
* __Pytest__
* __Requests__
* __Pytest-html__
* __Locust__
* __Python-dotenv__

The dependencies are also listed in requirements.txt

## Installation
Pre-requisite:
- Install Python from [here](https://www.python.org/downloads/ "here").
- git clone https://github.com/Rosh1988/movie-db-api-testing.git`
- cd to root folder
- rename .env_template to .env
- provide a valid API key for the variable 'valid_api_key' in the renamed file .env

__Install Pytest__
```shell
pip install -U pytest
```
__Install Requests__
```sh
pip install requests
```
__Install Pytest-html__ (required to generate html test report)
```sh
pip install pytest-html
```
__Install Locust__ (required for load testing)
```sh
pip install locust
```
__Install Python-dotenv__ (required to read environment variables from .env file)
```sh
pip install python-dotenv
```


> Note: You can also install all dependencies from requirements.txt using the command
"pip install -r requirements.txt"


## Automated API test

__To run a test, execute below command in terminal__

```sh
pytest
```

__To run and get details of all the executed test, execute below command in terminal__:
```sh
pytest -rA
```
> Note: Framework is configured to generate detailed html test report with the name "report.html". This is confiugured in pytest.ini by adding "--html=report.html" as a default command parameter.

## Load Test

__To run the load test, execute below command in terminal__

```sh
locust -f .\tests\load_test_movie.py
```
This command will start a web interface and display the url in the terminal. Go to the url in browser and enter the below parameters for the load testing:

- Number of users
- Spawn rate

__To run the load test without web interface, execute below command in terminal__

```sh
locust -f .\tests\load_test_movie.py --headless -u <# of users> -r <spawn rate> -t <total run time>

E.g. locust -f .\tests\load_test_movie.py --headless -u 2 -r 1 -t 10s
```

## Dockerfile

The project is containerized with a docker file (Dockerfile) which should be used to create image and run the project in container. The load testing framework and dependencies are not included in the Dockerfile.

## Test Scenarios

|Test ID   | Method | API Endpoint   | Test Name  |Test Steps   |Test Data   |Expected |
| :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
|1.1   |GET |3/movie/top_rated   |test_get_top_rated_movies_status_code_200   |Provide Valid API Key   |valid_api_key   |The response contains status code 200 & status message "Success."   |
|1.2  |GET   |3/movie/top_rated   |test_get_top_rated_movies_status_code_401   |Provide invalid API key   |invalid_api_key   |The response contains status code 401 & status message "Invalid API key: You must be granted a valid key."   |
|2.1   |PUT   |3/movie/{movie_id}/rating   |test_put_rate_movie_status_code_201   |Provide valid API key & valid movie id   |valid_api_key, valid_movie_id   |The response contains status code 201 & status message "Success."   |
|2.2   |PUT   |3/movie/{movie_id}/rating   |test_put_rate_movie_status_code_401   |Provide invalid API key & valid movie id   |invalid_api_key, valid_movie_id   |The response contains status code 401 & status message "Invalid API key: You must be granted a valid key."   |
|2.3   |PUT   |3/movie/{movie_id}/rating   |test_put_rate_movie_status_code_404   |Provide valid API key & invalid movie id   |valid_api_key, invalid_movie_id   |The response contains status code 401 & status message "The resource you requested could not be found."   |



