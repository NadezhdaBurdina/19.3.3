import requests

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers = {'accept':'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


#выполняем post запрос. Добавляем питомца

import json
info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Tom",
  "photoUrls": [
    "Tom's photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type':'application/json'}, data = json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())

#выполняем delete запрос

# res = requests.delete(url, **kwargs)


res = requests.delete(f"https://petstore.swagger.io/v2/pet", headers = {'accept':'application/json'}, data = json.dumps(info))

print(res.status_code)
print(res.text)
print(res.json())

# Выполняем put запрос
# res = requests.put(url, data=data)

new_info= {
  "id": 0,
  "category": {
    "id": 0,
    "name": "leopard"
  },
  "name": "Vasya",
  "photoUrls": [
    "no photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}


res = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(new_info, ensure_ascii=False))
print(res.status_code)
print(res.text)
print(res.json())