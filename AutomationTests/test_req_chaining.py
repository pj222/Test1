import requests
import json
import jsonpath

def test_adddata():
    global id
    url="https://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Python/add.json","r")
    request=json.loads(f.read())
    response=requests.post(url,request)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),"id")
    print(id[0])

def test_getdata():
    url = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    #url = "https://thetestingworldapi.com/api/studentsDetails/10088372)"
    req=requests.get(url)
    print(req.text)
