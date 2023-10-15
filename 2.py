import json

k = int(input("Введите количество продуктов для добавления: "))

pr = {"products":[]}
for i in range(k):
    name = input("Название: ")
    price = int(input("Цена: "))
    weight = int(input("Вес: "))
    available = bool(int(input("В наличии 0/1: ")))
    pr["products"].append({"name":name,"price":price,"weight":weight,"available":available})

with open("1.json") as f:
    inf = json.load(f)

inf["products"].extend(pr["products"])

for i in inf["products"]:
    print("Название: ", i["name"])
    print("Цена: ", i["price"])
    print("Вес: ", i["weight"])
    print("В наличии" if i["available"] else "Нет в наличии!","\n")

with open("1.json","w") as f:
    json.dump(inf, f, indent=4,ensure_ascii=False)
