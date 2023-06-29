import random

print(random.randint(2, 17))



def multiply(num1, num2):
    return num1*num2


n1 = input("Enter first number:")
n2 = input("Enter second number:")
result = multiply(int(n1), int(n2))
print(result)
