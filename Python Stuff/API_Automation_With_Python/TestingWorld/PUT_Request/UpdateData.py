import json
import requests as rq
import jsonpath as jp

url = "https://reqres.in/api/users/2"

# Loading JSON file
file = open("C:/Automation/Files/postAPI.json", "r")
file_data = file.read()
json_body = json.loads(file_data)
print("JSON body is: ", json_body)

# Making PUT Request
response = rq.put(url,json_body)

# Verifying Status code
assert response.status_code==200,"Data did not update."

json_response = json.loads(response.text)
job = jp.jsonpath(json_response,'job')
print("Job is:",job[0])
