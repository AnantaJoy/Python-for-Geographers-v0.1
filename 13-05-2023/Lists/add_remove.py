country = ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan", "Sri Lanka"]

# append list
country.append("Maldives")
print(country)

# insert list
country.insert(5, "Afganisthan")
print(country)

# remove
country.pop()
print(country)

# pop a particular item
country.pop(5)
print(country)

# remove
country.remove("Pakistan")
print(country)

# delete items
del country[0:2]
print(country) 