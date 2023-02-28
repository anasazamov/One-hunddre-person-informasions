import requests
import json

list=[]

for i in range(1,101):
    response = requests.get("https://randomuser.me/api").json()
    data = response["results"][0]
    user={}
    name = f'{data["name"]["first"]} {data["name"]["last"]}'
    user.setdefault("fullname",name)
    user.setdefault("country",data['location']["country"])
    user.setdefault("phone",data["phone"])
    user.setdefault("gender",data["gender"])
    list.append(user)
    
text=json.dumps(list)
text = text.replace(",",",\n\t",text.count(","))
text =text.replace("},","},\n\n",text.count("},"))
text=text.replace("]","\n]")

with open(".json",'w') as f:
    f.write(text)
