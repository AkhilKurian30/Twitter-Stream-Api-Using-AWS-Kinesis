import requests
import json

def searchApi(product):

    url = "https://gnip-api.twitter.com/search/%s/accounts/viralnation/prod/counts.json" % product


    headers= {
        "Content-Type": "application/json",
    }


    payload = json.dumps({
        "query": "from:sachin_rt",
       "fromDate":"200603210000",
       "bucket":"day"
    })

    response = requests.request("POST", url, headers=headers, data = payload, auth=('', ''))

    resp = json.loads(response.text)
    print(response.text)




# searchApi("30day")
searchApi("fullarchive")
