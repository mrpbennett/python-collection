import json

with open("HT-837.json") as f:
    data = json.load(f)

    for i in data:
        print(i["response"]["response"]["logEvent"][0]["deviceIfa"])
