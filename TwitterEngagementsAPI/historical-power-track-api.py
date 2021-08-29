import requests
import json

def addHistoricalPowerTrackJobs():


    url = "https://gnip-api.gnip.com/historical/powertrack/accounts/viralnation/publishers/twitter/jobs.json"

    headers= {
        "Content-Type": "application/json",
    }


    payload = json.dumps({
        "publisher": "twitter",
        "dataFormat":"original",
        "fromDate":"200603212051",
        "toDate":"202104010001",
        "title":"my_job123456",
        "rules":[{"value":"from:sachin_rt","tag":"tag1"}]
    })


    response = requests.request("POST", url, headers=headers, data = payload, auth=('','''))

    print(response.text)

    # Reponse
    # {"title":"my_job123","account":"viralnation","publisher":"twitter","streamType":"track_v2","format":"original","fromDate":"201201010000","toDate":"202101010001","requestedBy":"mgagliese@viralnation.com","requestedAt":"2021-04-07T06:15:18Z","status":"opened","statusMessage":"Waiting on quote from Gnip.","jobURL":"https://gnip-api.gnip.com:443/historical/powertrack/accounts/viralnation/publishers/twitter/jobs/eff5t4me1j.json","rules":{"summary":{"created":1,"not_created":0},"detail":[{"rule":{"value":"from:EldhoShaji8","tag":"tag1","id":8279946641681079174},"created":true}],"sent":"2021-04-07T06:15:18.783Z"}}




def getJobStatus():

    url = "https://gnip-api.gnip.com:443/historical/powertrack/accounts/viralnation/publishers/twitter/jobs/r5pr55bpyd.json"

    headers= {
        "Content-Type": "application/json",
    }

    response = requests.request("GET", url, headers=headers, auth=('','''))

    print(response.text)


def acceptJobs():

    url = "https://gnip-api.gnip.com/historical/powertrack/accounts/viralnation/publishers/twitter/jobs/r5pr55bpyd.json"

    headers= {
        "Content-Type": "application/json",
    }

    payload = json.dumps({
        "status": "accept"
    })

    response = requests.request("PUT", url, headers=headers, data=payload, auth=('','''))

    print(response.text)


    # {"title":"my_job123456","account":"viralnation","publisher":"twitter","streamType":"track_v2","format":"original","fromDate":"200603212051","toDate":"202104010001","requestedBy":"mgagliese@viralnation.com","requestedAt":"2021-04-07T12:19:44Z","status":"quoted","statusMessage":"Job quoted and awaiting customer acceptance.","jobURL":"https://gnip-api.gnip.com:443/historical/powertrack/accounts/viralnation/publishers/twitter/jobs/r5pr55bpyd.json","quote":{"estimatedActivityCount":100,"estimatedDurationHours":"915.0","estimatedFileSizeMb":"0.0","expiresAt":"2021-04-14T14:33:52Z"},"percentComplete":0}

    # {"title":"my_job12345","account":"viralnation","publisher":"twitter","streamType":"track_v2","format":"original","fromDate":"202101010000","toDate":"202104010001","requestedBy":"mgagliese@viralnation.com","requestedAt":"2021-04-07T09:34:20Z","status":"accepted","statusMessage":"Job accepted and ready to be queued.","jobURL":"https://gnip-api.gnip.com:443/historical/powertrack/accounts/viralnation/publishers/twitter/jobs/nmj5xf3z21.json","quote":{"estimatedActivityCount":100,"estimatedDurationHours":"20.0","estimatedFileSizeMb":"0.0","expiresAt":"2021-04-14T09:50:14Z"},"acceptedBy":"mgagliese@viralnation.com","acceptedAt":"2021-04-07T11:26:45Z"}



def getResults():

    url = "https://gnip-api.gnip.com/historical/powertrack/accounts/viralnation/publishers/twitter/jobs/nmj5xf3z21/results.json"
    
    headers= {
        "Content-Type": "application/json",
    }

    response = requests.request("GET", url, headers=headers, auth=('','''))

    print(response.text)


# addHistoricalPowerTrackJobs()
# getJobStatus()
acceptJobs()
# getResults()



# nmj5xf3z21 - EldhoShaji8
# r5pr55bpyd - sachin_rt

