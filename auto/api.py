import requests
import allure
import json


class ApiRequests:

    def __init__(self, url):
        self.url = url

    @allure.step("Добавление товара в корзину")
    def add_prod(self):
        headers = {
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Cookie': 'PHPSESSID=9Os7fg32RAGHyOLnCDzMQPz17Yfy48fu',
           'accept': 'application/json, text/javascript, */*; q=0.01'
        }
        data_json = {"idCookie": "810568", "idProd": "180", "type": "add"}
        data = f'data={json.dumps(data_json)}'
        resp = requests.post(self.url, headers=headers, data=data)
        json_response = resp.json()
        return json_response


    @allure.step("Уведичение количества товара")
    def increase_prod(self):
        headers = {
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Cookie': 'PHPSESSID=9Os7fg32RAGHyOLnCDzMQPz17Yfy48fu',
           'accept': 'application/json, text/javascript, */*; q=0.01'
        }
        data_json = {"idCookie": "810568", "idProd": 180 ,"type": "plus"}
        data = f'data={json.dumps(data_json)}'
        resp = requests.post(self.url, headers=headers, data=data)
        json_response = resp.json()
        return json_response

    @allure.step("Удаление товара")
    def reduction_prod(self):
        headers = {
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Cookie': 'PHPSESSID=9Os7fg32RAGHyOLnCDzMQPz17Yfy48fu',
           'accept': 'application/json, text/javascript, */*; q=0.01'
        }
        data_json = {"idCookie": "810568", "idProd": 180, "type": "minus"}
        data = f'data={json.dumps(data_json)}'
        resp = requests.post(self.url, headers=headers, data=data)
        json_response = resp.json()
        return json_response
