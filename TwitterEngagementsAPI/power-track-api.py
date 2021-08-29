import requests
import json


def addRulesPowerTrackAPI():

    url = "https://data-api.twitter.com/rules/powertrack/accounts/viralnation/publishers/twitter/prod.json"

    headers= {
        "Content-Type": "application/json",
    }

    payload = json.dumps({
        "rules":
        [
            {"value":"nike","tag":"tag1"},
        ]
    })

    response = requests.request("POST", url, headers=headers, data = payload, auth=('','''))
    print(response.text)


def streaming():

    s = requests.Session()

    headers = {"Content-Type": "application/json"}
    req = requests.Request("GET",'https://gnip-stream.twitter.com/stream/powertrack/accounts/viralnation/publishers/twitter/prod.json',
                           headers=headers, auth=('',''')).prepare()

    resp = s.send(req, stream=True)

    for line in resp.iter_lines():
        if line:
            yield line


def readStream():

    for line in streaming():
        print(line)
        data = json.loads(line)



# addRulesPowerTrackAPI()
readStream()



