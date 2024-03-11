import requests
import json
import jsonpath

def test_add():
    url="https://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Python/e2eadd.json","r")
    req_json=json.loads(f.read())
    response_json=requests.post(url,req_json)
    id=jsonpath.jsonpath(response_json.json(),"id")
    print(id[0])

    techurl="https://thetestingworldapi.com/api/technicalskills"
    f=open("C:/Python/addtechskils.json","r")
    jsonres=json.loads(f.read())
    jsonres['id']=int(id[0])
    jsonres['st_id']=id[0]
    response1 = requests.post(techurl, jsonres)
    #print(response1.text)

    addressurl="https://thetestingworldapi.com/api/addresses"
    f = open("C:/Python/add_address.json", "r")
    res=json.loads(f.read())
    res['st_id']=id[0]
    jresponse=requests.post(addressurl,res)
    #print(jresponse.text)

    finalurl="https://thetestingworldapi.com/api/FinalStudentDetails/+str(id[0])"
    final_response=requests.get(finalurl)
    print(final_response.text)