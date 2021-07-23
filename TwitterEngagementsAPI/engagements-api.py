import requests
import json


def engagementsAPI():

    url = "https://data-api.twitter.com/insights/engagement/totals"

    headers= {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACh3OQEAAAAAJppetMF2dySZzpeKQJ94qER0lyA%3DY0yiOm841nsmCWzijRkO163IpTDeNXQSYX3lo2VuoBTLXceTcv"
    }

    payload = json.dumps({
        "tweet_ids": ["1334663832849981440"],
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


    # curl --request POST 
    # --url https://data-api.twitter.com/insights/engagement/totals 
    # --header 'accept-encoding: gzip' 
    # --header 'authorization: Bearer ' 
    # --header 'content-type: application/json' 
    # --data '{
    #                 "tweet_ids": [
    #                     "1070059276213702656","1021817816134156288","1067094924124872705"
    #                 ],
    #                 "engagement_types": [
    #                     "favorites","retweets","replies","quote_tweets","video_views"
    #                 ],
    #                 "groupings": {
    #                     "perTweetMetricsUnowned": {
    #                         "group_by": [
    #                             "tweet.id",
    #                             "engagement.type"
    #                         ]
    #                     }
    #                 }
    #             } 
    # --verbose 
    # --compressed

engagementsAPI()


