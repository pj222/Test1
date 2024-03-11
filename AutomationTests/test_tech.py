import requests
import json
import jsonpath
def test_addtech():
    techurl="https://thetestingworldapi.com/api/technicalskills"
    f=open("C:/Python/addtechskils.json","r")
    jsonres=json.loads(f.read())
    #jsonres['id']=int(id[0])
    #jsonres['st_id']=id[0]
    response1 = requests.post(techurl, jsonres)
    id=jsonpath.jsonpath(response1.json(),"id")
    print(id)
    gettechurl="https://thetestingworldapi.com/api/technicalskills/+str(id[0]"
    getresponse=requests.get(gettechurl)
    print(getresponse.text)