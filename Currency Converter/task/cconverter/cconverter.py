# write your code here!

import requests
import json
# user_input = input()
# exchange_rate = requests.get(f"http://www.floatrates.com/daily/{user_input}.json")
# json_to_dict = exchange_rate.json()
# print(json_to_dict["usd"])
# print(json_to_dict["eur"])


user_currency = input()
# foreign_currency = input()
# amt_to_exchange = float(input())
cache = {}
exchange_rates = requests.get(f"http://www.floatrates.com/daily/{user_currency}.json")
json_to_dict = exchange_rates.json()
# cache[user_currency] = json_to_dict
# while True:
#     foreign_currency = input()
#     if foreign_currency == "":
#         break
#     else:
#         amt_to_exchange = float(input())
#         print("Checking the cache...")
#         if foreign_currency in cache[user_currency]:
#             print("Oh! It is in the cache!")
#             amt_to_recv = cache[user_currency][foreign_currency]["rate"] * amt_to_exchange
#             print(f"You received {round(amt_to_recv, 2)} {foreign_currency.upper()}")



if user_currency == "usd":
    cache["eur"] = json_to_dict["eur"]["rate"]
elif user_currency == "eur":
    cache["usd"] = json_to_dict["usd"]["rate"]
else:
    cache["usd"] = json_to_dict["usd"]["rate"]
    cache["eur"] = json_to_dict["eur"]["rate"]

while True:
    foreign_currency = input()
    if foreign_currency == "":
        break
    else:
        amt_to_exchange = float(input())
        print("Checking the cache...")
        if foreign_currency in cache:
            print("Oh! It is in the cache!")
            amt_to_recv = cache[foreign_currency] * amt_to_exchange
            print(f"You received {round(amt_to_recv, 2)} {foreign_currency.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            cache[foreign_currency] = json_to_dict[foreign_currency]["rate"]
            amt_to_recv = cache[foreign_currency] * amt_to_exchange
            print(f"You received {round(amt_to_recv, 2)} {foreign_currency.upper()}.")



