import requests, json
from .authHelpers import fetch_jwt_token

# config = {}
# with open('./config.json') as config_file:
# 	config = json.load(config_file)

url = "http://127.0.0.1:5000/projects"

class Project:

    def createProject(self, data):
        jwt = fetch_jwt_token(data["workspace"], data["user"])
        response = requests.post(url= url, json= data, headers={"bearer-token": jwt}).json()
        return response
    
    def getProject(self, data):
        jwt = fetch_jwt_token(data["workspace"], data["user"])
        getUrl = url + '/' + data["taskId"]
        response = requests.get(url = getUrl, headers={"bearer-token": jwt}).json()
        return response

