import requests, json
from .authHelpers import store_jwt_token

# config = {}
# with open('./config.json') as config_file:
# 	config = json.load(config_file)

url = "http://127.0.0.1:5000/user"

class User:

    def signup_user(self, data):
        req_url = url + '/signup'
        response = requests.post(url= req_url, json= data).json()
        return response[0]

    def login_user(self, data):
        req_url = url + '/login'
        response = requests.post(url= req_url, json= data).json()
        return response

