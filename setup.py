import json
import requests

with open("config.json", "r") as f:
    config = json.load(f)

clauses = config["clauses"]

API_URL = f"https://codeforces.com/api/contest.status?contestId={config['contestId']}"
request = requests.get(API_URL)
if(request.status_code != 200):
    print(f"Error: {request.status_code}")
    exit()

submissions = request.json()
if submissions["status"] != "OK":
    print("Error: Bad Request")
    exit()

submissions = submissions["result"]

with open("contest.json", "w") as f:
    f.write(json.dumps(submissions))