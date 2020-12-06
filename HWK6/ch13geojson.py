import urllib.request, urllib.parse, urllib.error
import json

serviceurl = ('http://maps.googleapis.com./maps/apigeocode/json?') 

while True:
    address = input('Enter Location: ' )
    if len(address) < 1: break

    url = serviceurl + urllib.parse(
        {'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads, (data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(json.dumps(js, indent=4))

    lat = js ["results"] [0] ["geometry"] ["location"] ["lat"]
    lng = js ["results"] [0] ["geometry"] ["location"] ["lng"]
    print('lat', lat) 
    print('lng', lng )
    location = js ['results'] [0] ['formatted address']
    print(location)