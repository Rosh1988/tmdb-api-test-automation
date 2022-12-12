import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

base_url = os.getenv('base_url')
print(base_url)


def get_api(api, api_key):
    r = requests.get(f'{base_url}/{api}?api_key={api_key}&language=en-US&page=1')
    return r.status_code, r.json()

def get_guest_session_id(api, api_key):
    r = requests.get(f'{base_url}/{api}?api_key={api_key}')
    return r.json()['guest_session_id']

def put_api(api, api_key, gsid, rdata):
    r = requests.post(f'{base_url}/{api}?api_key={api_key}&guest_session_id={gsid}',
    headers={"Content-Type": "application/json;charset=utf-8"},
    data=rdata)
    return r.status_code, r.json()