import json
import requests as rq
import jsonpath as jp

url = "https://reqres.in/api/users"

# Loading JSON file
file = open("C:/Automation/Files/postAPI.json", "r")
file_data = file.read()
json_body = json.loads(file_data)
print("JSON body is: ", json_body)

# Making POST Request using JSON Input Body
response = rq.post(url, json_body)

# Validating status code
assert response.status_code == 201, "Data is not created."

# Fetching Header
print("Headers: ",response.headers)
print("Content length: ",response.headers.get('Content-Length'))

# Fetching Id
json_response = json.loads(response.text)
id = jp.jsonpath(json_response,'id')
print("Id is: ",id[0])