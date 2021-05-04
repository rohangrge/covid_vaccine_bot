import requests
import json
import redis

url = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'

re = redis.Redis()
r = requests.get(url)
data = json.loads(r.content)
# print(data['states'])
a = []
for i in data['states']:
    print(i)
    re.set(i['state_name'].lower()+'_sid', i['state_id'])
    a.append(i['state_name'])

print(a)
