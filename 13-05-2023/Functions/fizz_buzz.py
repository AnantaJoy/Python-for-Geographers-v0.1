# Fizz Buzz 
# Write a program that prints the numbers 
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else: 
        return num
    

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))
print(fizz_buzz(10))