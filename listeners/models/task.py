import requests, json
from .authHelpers import fetch_jwt_token

# config = {}
# with open('./config.json') as config_file:
# 	config = json.load(config_file)

url = "http://127.0.0.1:5000/tasks"

class Task:

    def createTask(self, data):
        jwt = fetch_jwt_token(data["workspace"], data["user"])
        response = requests.post(url= url, json= data, headers={"bearer-token": jwt}).json()
        return response

    def findTask(self, data):
        jwt = fetch_jwt_token(data["workspace"], data["user"])
        response = requests.patch(url = url, json= data["filterValue"], headers={"bearer-token": jwt}).json()
        return response
    
    def getTask(self, data):
        jwt = fetch_jwt_token(data["workspace"], data["user"])
        getUrl = url + '/' + data["taskId"]
        response = requests.get(url = getUrl, headers={"bearer-token": jwt}).json()
        return response
        
    def deleteTask(self, data):
        jwt = fetch_jwt_token(data["workspace"], data["user"])
        deleteUrl = url + '/' + data["taskId"]
        response = requests.delete(url= deleteUrl, headers={"bearer-token": jwt}).json()
        return response
    
    def updateTask(self, data):
        jwt = fetch_jwt_token(data["workspace"], data["user"])
        print(jwt)
        putUrl = url + '/' + data["id"]
        response = requests.put(url = putUrl, json= data, headers={"bearer-token": jwt}).json()
        return response

