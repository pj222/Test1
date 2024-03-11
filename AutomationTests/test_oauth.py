import json
import requests
import jsonpath
from requests.auth import HTTPBasicAuth

def test_oauthtest():
    tokenurl="http://thetestingworldapi.com/Token"
    data={'grant_type':'password','username':'pj222','password':'Shreeram@24'}
    response=requests.post(tokenurl,data)
    res=requests.get(url, auth=HTTPBasicAuth("pj222", "Shreeram@24"))
    print(res.text)