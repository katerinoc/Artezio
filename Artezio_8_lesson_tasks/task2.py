"""task 2"""
import requests


def value_converter(money,base,finish_value):
    url = "https://api.exchangerate-api.com/v4/latest/" + base
    url_request = requests.get(url)
    url_request = url_request.json()
    rates = url_request["rates"]
    from_rate = rates[finish_value]
    result = from_rate * money
    return result


print(value_converter(10, 'USD', 'RUB'))
