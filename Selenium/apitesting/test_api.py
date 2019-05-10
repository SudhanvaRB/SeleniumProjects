'''
Created on Dec 19, 2018

@author: subharad
'''
import requests 
import json



s = requests.Session()
para = {'page': 4}
base_url = "https://reqres.in" 
s.proxies = {"https": "http://blrproxy.igate.com:8080"}

response = s.get(base_url + "/api/users" , params=para , verify=False)
#print(response.json())
print(json.dumps(response.json() , indent = 4))

print(response.status_code)

