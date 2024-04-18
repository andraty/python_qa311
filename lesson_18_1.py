import requests

# responce = requests.get("https://randomuser.me/api/")
# print(responce.status_code) # 200
# print(responce.reason) # OK
# print(responce.text)


responce_2 = requests.get("https://api.thedogapi.com/v1/breeds")



# print(type(responce_2))
# print(type(responce_2.json()[2]))

new_dog_firstLetter_C = []
# for i in range(len(responce_2.json())):

for i in range(len(responce_2.json())):
    if responce_2.json()[i]["name"][0] == "I":
        new_dog_firstLetter_C.append(responce_2.json()[i]["name"])

print(new_dog_firstLetter_C)