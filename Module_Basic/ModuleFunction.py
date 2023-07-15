import random

print(random.randint(2, 17))

# =============================================================

def multiply(num1, num2):
    #  a sample function that take 2 arguments an return a value
    return num1*num2


n1 = input("Enter first number:")
n2 = input("Enter second number:")
result = multiply(int(n1), int(n2))
print("the result value is= "+str(result))
# print(result)
# =============================================================
