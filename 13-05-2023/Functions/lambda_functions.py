price_list = [
    ('Product1', 13),
    ('Product2', 6),
    ('Product3', 8),
    ('Product4', 5),
]

# sorting product by price
price_list.sort(key=lambda item: item[1])
print(price_list)