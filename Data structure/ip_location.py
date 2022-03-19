
import requests
import json

# #----------   single ip request   ------------


# response = requests.get("http://ip-api.com/json/24.48.0.1").json()
# print(response)

# print(response['country'])



# #----------   batch ip  request   -------------


# response = requests.post("http://ip-api.com/batch", json=[
#     {"query":"208.80.152.201"},
#     {"query":"168.71.3.52"},
#     {"query":"206.189.198.234"},
#     {"query":"157.230.75.212"}
# ]).json()

# for ip_info in response:
#         print(ip_info["country"])
#         print(ip_info["country"])



# IP address to test
ip_address = '187.32.952.189'

# URL to send the request to
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()
# Clean the returned string so it just contains the dictionary data for the IP address
result = result.split("(")[1].strip(")")
# Convert this data into a dictionary
result  = json.loads(result)
print(result)
