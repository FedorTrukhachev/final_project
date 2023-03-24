import configurations
import requests
import data

#создание нового заказа
def post_new_order(body):
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_ORDER,
                        json=body)

response = post_new_order(data.user_body)
print(response.json())
print(response.status_code)
track = response.json()
print(track)


#получение заказа
def get_take_an_order():
    params_dict = data.track_order.copy() #создаём переменню для копирования данных в словаре
    params_dict["t"] = track["track"] #изменяем данные в словаре
    return requests.get(configurations.URL_SERVICE + configurations.GET_ORDER,
                        params=params_dict
                        )

response = get_take_an_order()

print(response.json())
print(response.status_code)
print(response.url)
