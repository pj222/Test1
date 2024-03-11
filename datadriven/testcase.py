import requests
import json
import jsonpath
import openpyxl
import library


def test_add_multipledata():
    apiurl = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Python/add.json")
    json_request = json.loads(f.read())
    obj=library.common("C:/Python/add_data.xlsx","Sheet1")
    row=obj.fetch_row()
    col=obj.fetch_cols()
    keylist=obj.fetch_keynames()

    for i in range(2,row+1):
     updated_jsonreq=obj.insertvalue(i,json_request,keylist)
     responae=requests.post(apiurl,updated_jsonreq)

     print(responae.text)
     print(responae.content)
     print(responae.status_code)
