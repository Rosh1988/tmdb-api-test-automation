import os
from locust import HttpUser, task
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

valid_api_key = os.getenv('valid_api_key')
base_url = os.getenv('base_url')

class WebsiteUser(HttpUser): 
    host = base_url

    @task 
    def load_test_get_top_rated_movies(self):
        self.client.get(f'/3/movie/top_rated?api_key={valid_api_key}')
