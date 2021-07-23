import requests
import json

def searchApi(product):

    url = "https://gnip-api.twitter.com/search/%s/accounts/viralnation/prod.json" % product


    headers= {
        "Content-Type": "application/json",
    }


    payload = json.dumps({
        "query": "from:sachin_rt",
        "maxResults":"500",
        "fromDate": "200603210000"
    })

    response = requests.request("POST", url, headers=headers, data = payload, auth=('akurian@menervasoftware.com', 'miAkhil@242387'))

    resp = json.loads(response.text)
    print(response.text)




# searchApi("30day")
searchApi("fullarchive")
