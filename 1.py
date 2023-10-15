import json

with open("1.json",encoding='utf-8') as f:
    inf = json.load(f)

for i in inf["products"]:
    print("Название: ", i["name"])
    print("Цена: ", i["price"])
    print("Вес: ", i["weight"])
    print("В наличии" if i["available"] else "Нет в наличии!","\n")

