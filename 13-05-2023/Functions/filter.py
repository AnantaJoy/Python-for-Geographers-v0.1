price_list = [
    ('Product1', 13),
    ('Product2', 6),
    ('Product3', 8),
    ('Product4', 5),
]

# filtering product by price
filtered = list(filter(lambda item: item[1] >= 10, price_list))
print(filtered)