price_list = [
    ('Product1', 13),
    ('Product2', 6),
    ('Product3', 8),
    ('Product4', 5),
]

# mapping product by price
prices = []

for item in price_list:
    prices.append(item[1])
print(prices)   

price = map(lambda item: item[1], price_list)
print(price)
for item in price:
    print(item)

price = list(map(lambda item: item[1], price_list))
print(price)