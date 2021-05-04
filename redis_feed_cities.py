import requests
import json
import redis
r = redis.Redis()
states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
          'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
url = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts'
for i in states:
    v = str(r.get(i.lower()+'_sid').decode('utf-8'))
    print(v)

    try:
        url1 = url+'/'+v
        re = requests.get(url1)
        # print(url1)
        data = re.content
        # print(data)
        con = json.loads(data)
        for j in con['districts']:
            print(j)
            r.set(j['district_name'].lower()+'_cid', j['district_id'])
    except:
        print('fail')
