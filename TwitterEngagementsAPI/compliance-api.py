import requests
import json


def complianceAPI():

    url = "https://gnip-api.gnip.com/historical/powertrack/accounts/viralnation/publishers/twitter/jobs/nmj5xf3z21.json"


    url = "https://gnip-stream.twitter.com/stream/compliance/accounts/viralnation/publishers/twitter/compliance.json?partition=1"

    headers= {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer "
    }

    payload = json.dumps({
        "tweet_ids": ["1377212274192961540"],
        "engagement_types": ["favorites","retweets","replies","quote_tweets","video_views"],
        "groupings": {
            "perTweetMetricsUnowned": {
                "group_by": [
                    "tweet.id",
                    "engagement.type"
                ]
            }
        }
    })

    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text)


complianceAPI()


