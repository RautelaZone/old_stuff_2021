import requests as rq

url = "https://reqres.in/api/users/2"

#Sending DELETE request
response = rq.delete(url)

status_code = response.status_code
print(status_code)
assert status_code==204, "Delete request did not process."
