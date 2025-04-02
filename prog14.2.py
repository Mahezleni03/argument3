def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
print("Factorial of 0 : ",factorial(0))
print("Factorial of 10 : ",factorial(10))