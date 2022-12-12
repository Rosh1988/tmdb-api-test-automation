from locust import HttpUser, task

valid_api_key = '85e760da8dc8acd92ab9b3feaae90e20'    

class WebsiteUser(HttpUser): 
    host = "https://api.themoviedb.org"

    @task 
    def load_test_get_top_rated_movies(self):
        self.client.get('/3/movie/top_rated?api_key=85e760da8dc8acd92ab9b3feaae90e20')
