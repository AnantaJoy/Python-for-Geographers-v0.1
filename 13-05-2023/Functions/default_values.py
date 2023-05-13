# default parameters are parameters that have a default value
# if no value is passed in for that parameter, the default value is used
# default parameters must be at the end of the parameter list

def discouted_price(price, rate=0.1):
    return price - (price * rate)

price = 500
print(discouted_price(price))

# if you want to pass in a value for the second parameter, you must specify the parameter name
print(discouted_price(price, rate=0.2))
print(discouted_price(price, 0.5))
