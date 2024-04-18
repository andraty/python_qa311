import requests

# стандартное получение запроса api
req = requests.get("https://randomuser.me/api/")
print(req.status_code)
print(req.text)

# api к сайту с собаками
req_1 = requests.get("https://api.thedogapi.com/v1/breeds")
print(req_1.status_code) # статус ответа цифрами
print(req_1.reason) # статус ответа словами
print(req_1.text)

# проверка заголовков ответа
print(req_1.headers)

# заголовки запроса который получает сервер когда мы к нему обращаемся
print(req_1.request.headers)

# изменение заголовка в запросе
headers = {"User-Agent":"Iphone 17"}
resp = requests.get("https://api.thedogapi.com/v1/breeds", headers=headers)
# print(resp.request.headers)

# можно получить какой-то конкретный элемент заголовка
print(resp.headers.get("Content-Type"))

# представление в виде json
print(resp.json()[0]["name"])

# print(resp[0]["name"])

# параметры запороса gender и nat
resp_1 = requests.get("https://randomuser.me/api/?gender=female&nat=de").json()
print(resp_1)

# параметры запроса можно передать в виде
param = {"gender":"female", "nat":"de"}
resp_1 = requests.get("https://randomuser.me/api/", params=param).json()
print(resp_1)

# параметры запроса строго документированы
# передаем запрос и строку запроса поотдельности
query_param = {"q":"Affenpinscher"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
resp_2 = requests.get(endpoint, params=query_param).json()
print(resp_2)


# случаи когда необходимо ввести ключ
endpoint_1 =  "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Замените DEMO_KEY ниже своим собственным ключом, если вы его сгенерировали.
api_key = "jUJ6DnVp0rcWvotPq6mJn9s0gfGhzQeiqoqgXPTc"
query_param = {"api_key": api_key, "earth_date": "2020-07-01"}
resp_3 = requests.get(endpoint_1, params=query_param).json()
print(f"Найден {len(resp_3['photos'])}")

