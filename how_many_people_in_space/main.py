import json
import requests

response=requests.get("http://api.open-notify.org/astros.json")
numberinspace=response.json()["number"]

print("People's names in space:")

for index,human in enumerate(response.json()["people"]):
    print("{}) {} -> {}".format(index,human["name"],human["craft"]))


print("People number in space: {}".format(numberinspace))
