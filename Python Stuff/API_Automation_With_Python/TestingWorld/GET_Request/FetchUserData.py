import requests as rq
import jsonpath as jp
import json
from jsonpath_ng import *

url = "https://reqres.in/api/users?page=2"

#Sending GET request
response = rq.get(url)
res_content = response.content
print("Content: ",res_content)
print("Header: ",response.headers)
print("Status code is:", response.status_code)

json_response = json.loads(response.text)
pages = jp.jsonpath(json_response,'per_page')
per_page_value = pages[0]
print("Per Page Value is:", per_page_value)
assert per_page_value==6,"Value did not match"

# jsonpath_expression = parse('$.data.0,id')
# match = jsonpath_expression.find(json_response)
# print(match)