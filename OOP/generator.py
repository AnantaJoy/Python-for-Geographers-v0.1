def mygenerator(n):
    for i in range(n):
        yield i
        
print(mygenerator(5))
print(type(mygenerator))