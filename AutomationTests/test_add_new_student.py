import requests
import json
import jsonpath

def test_addstudent():
    apiurl="https://thetestingworldapi.com/api/studentsDetails"
    file=open("C:/Python/add.json","r")
    f1=file.read()
    jload=json.loads(f1)
    jpost=requests.post(apiurl,jload)
    print(jpost.text)
#def test_getstud():
 #   url="https://thetestingworldapi.com/api/studentsDetails/10087915"
  #  req=requests.get(url)
   # print(req.text)
    #jres=json.loads((req.text))
    #id=jsonpath.jsonpath(jres,"data.id")
    #print(id)
    #assert id[0]==10087915
def test_updatedata():
    url="https://thetestingworldapi.com/api/studentsDetails/10087915"
    file=open("C:/Python/update.json","r")
    res=json.loads(file.read())
    putres=requests.put(url,res)
    print(putres.text)
    #fname=jsonpath.jsonpath(putres,"data.first_name")
    #mname = jsonpath.jsonpath(putres, "data.middle_name")
def test_getstud():
    url="https://thetestingworldapi.com/api/studentsDetails/10087915"
    req=requests.get(url)
    jres=json.loads((req.text))
    print(jres)
def test_delete():
    url="https://thetestingworldapi.com/api/studentsDetails/10087915"
    req=requests.delete(url)
    print(req.text)


