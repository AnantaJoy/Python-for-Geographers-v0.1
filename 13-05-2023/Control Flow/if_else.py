# weathter forecast

weather = input("What is the weather today? ")

if weather == "rainy":
    print("Take an umbrella")
elif weather == "sunny":
    print("Take a hat")
elif weather == "windy":
    print("Take a jacket")
else:
    print("Enjoy the weather")
    

temperature = int(input("What is the temperature today? "))

if temperature > 30:
    print("It is hot")
    print("Drink more water")
elif temperature < 10:
    print("It is cold")
    print("Wear a jacket")
else:
    print("It is great weather")