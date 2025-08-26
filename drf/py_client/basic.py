import requests

# endpoint ="https://httpbin.org/status/200/"
# endpoint ="https://httpbin.org/anything"

endpoint = "http://127.0.0.1:8000/api/hello/"


get_response = requests.get(endpoint,params={"abc":123},json ={"title":"Hello world from post", "content":"this is just a content","price":345})
print(get_response.text)
print(get_response.status_code)