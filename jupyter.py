import requests
 
url = "http://localhost:8888/notebooks/Untitled10.ipynb?kernel_name=python3"
 
querystring = {"search.sessiontype":"1522435540042001BxTD"}
 
payload = {
    "import": "os",
    "print": "hello world"

}
headers = {
    'content-type': "application/json",
    'Token': "token=479173886e7d51a22d5e5e8b591bb7a8f5ec381a45477c7d"
    }
 
response = requests.request("POST", url, data=payload, headers=headers)
print(dir(response))
print(response.json)
#print first 4000 characters


