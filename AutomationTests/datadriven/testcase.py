import requests
import json
import jsonpath
import openpyxl
import AutomationTests.datadriven.library




def test_add_multipledata():
    apiurl = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Python/add.json", "r")
    json_request = json.loads(f.read())

    obj = library.common("C:/Python/add_data.xlsx", "Sheet1")
    r = obj.fetch_row()
    c = obj.fetch_cols()
    k = obj.fetch_keynames()

    for i in range(2, r + 1):
        updated_json_req = obj.insertvalue(i, json_request, k)
        response=requests.post(apiurl,updated_json_req)
        print(response.text)
