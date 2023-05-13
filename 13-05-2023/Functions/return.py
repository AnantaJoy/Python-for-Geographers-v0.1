# sum of two integers

def sum(a, b):
    return a + b

print(sum(1, 2))
print(sum(3, 4)+5)


# greet user function
def greetUser(name):
    return f'Hello ' + name + '!' # f-string

message = greetUser('Jesse')

# write message to file
file = open('./test.txt', 'w')
file.write(message)