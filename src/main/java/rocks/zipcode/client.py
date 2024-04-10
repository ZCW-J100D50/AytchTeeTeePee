import http.client

try:
    connection = http.client.HTTPConnection("localhost:8000")
    connection.request("GET", "/foo")
    response = connection.getresponse()
    print(response)
    print("Status: {} and result: {}".format(response.status, response.read()))
    connection.close()
except Exception as e:
    print("Error: {}".format(e))
