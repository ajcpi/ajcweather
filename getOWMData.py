import requests
import json
import datetime


CITYIDMAP = {
    "TAICHUNG": {"_id":1668399,"name":"Taichung","country":"TW","coord":{"lon":120.683899,"lat":24.1469}},
    "LOMBARD":  {"_id":4900373,"name":"Lombard","country":"US","coord":{"lon":-88.007843,"lat":41.880032}},
    "MAYNARD":  {"_id":4943490,"name":"Maynard","country":"US","coord":{"lon":-71.449509,"lat":42.43343}},
    "PORTLAND": {"_id":5746545,"name":"Portland","country":"US","coord":{"lon":-122.676208,"lat":45.523449}},
}
OWMKEY = '5c58fabe3cda1be2e8a6e5a1e2b5580d'

CURRENT_WEATHERS = "http://api.openweathermap.org/data/2.5/group?id=%s&APPID=%s&units=imperial"
CURRENT_WEATHER =  "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=imperial"

last_request = datetime.datetime(2000,1,1)

citylist = ",".join([ str(CITYIDMAP[k]["_id"]) for k in CITYIDMAP.keys() ])
if ((datetime.datetime.now() - last_request).seconds  > 15*60):
    resp = requests.get(CURRENT_WEATHERS % (citylist, OWMKEY))
    if resp.ok:
        last_request = datetime.datetime.now()
        wdict = resp.json()
