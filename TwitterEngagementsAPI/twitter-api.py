import requests
import json



bearerToken = "AAAAAAAAAAAAAAAAAAAAAMNCNAEAAAAADN%2BIKOlHzcyObnSv8f3pxNXCaR0%3DvzufJtYIx1rOTSx3VCiFrw7oUjiTP7Ix83pEyjmr5o0ilNfk81"
apiKey  = "wgqGwGufa7uIDZ7o8u2uGyUnr"
apiKeySecret = "mlx8l8Q8BIajdZtNOp9usBojK7kaW4vBFBn4bl5GjbzrpGcRCD"

headers= {
    "Content-Type": "application/json",
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAMNCNAEAAAAADN%2BIKOlHzcyObnSv8f3pxNXCaR0%3DvzufJtYIx1rOTSx3VCiFrw7oUjiTP7Ix83pEyjmr5o0ilNfk81"
}


def addRules():
    payload = json.dumps({
        "add": [
            {
                "value": "nike",
                "tag": ""
            }
        ]
    })
    # url = "https://api.twitter.com/2/tweets/search/stream/rules"

    # payload = "{\n    \"add\": [\n        {\n            \"value\": \"tostones recipe\"\n        }\n    ]\n}"


    # response = requests.request("POST", url, headers=headers, data = payload)

    # print(response.text.encode('utf8'))


    url = "https://api.twitter.com/2/tweets/search/stream/rules?dry_run=true"

    # payload = "{\n    \"add\": [\n        {\n            \"value\": \"tostones recipe\"\n        }\n    ]\n}"

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

# b'{"data":[{"value":"nike","tag":"","id":"1364459511319130119"}],"meta":{"sent":"2021-02-24T06:17:52.613Z","summary":{"created":1,"not_created":0,"valid":1,"invalid":0}}}'


def getRules():

    url = "https://api.twitter.com/2/tweets/search/stream/rules"

    payload = {}

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


def streamData():

    url = "https://api.twitter.com/2/tweets/search/stream"

    payload = {}
    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

addRules()
# getRules()
# streamData()


# def sampledStream():

#     url = "https://api.twitter.com/2/tweets/sample/stream"

#     payload = {}
#     response = requests.request("GET", url, headers=headers, data = payload)

#     print(response.text.encode('utf8'))

# sampledStream()




