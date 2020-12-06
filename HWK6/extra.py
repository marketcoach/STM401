data = json.loads(res.text)["features"] 
file = open("earthquake.txt","w") 
for i in data: 
    s = "A {mag} magnitude earthquake was recorded {place}"
format(mag=i["properties"]["mag"]), 
place = i(["properties"]["place"]) 
file.write(s) 
print(s) 