import requests
import json

reg='https://cit-home1.herokuapp.com/api/ga_homework'
txt = json.dumps({'1':{"value": 4351, "weight": 13000, "volume": 12,"items":[2, 3, 4, 6, 10, 15, 16, 18, 19, 20, 23, 26, 28, 29]},
'2':{"value": 4134, "weight": 11173, "volume": 12,"items":[1, 3, 4, 6, 8, 10, 15, 16, 18, 20, 21, 24, 28, 29]}})
head={'content-type': 'application/json'}

p = requests.post(reg, data=txt, headers=head)
print(p)
print(p.json())
