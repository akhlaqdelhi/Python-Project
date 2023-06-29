print(" \n Here we will learn some basic")

# define diffretn type of variables
product_quantity = 15
product_price = 9.25        # this is a float variable
customer_name = "Peter"
date_of_birth = '2010-05-20'

print("customerName: " + customer_name)
print(product_price)
print(date_of_birth)
product_quantity += 5   # reassigning value
print(product_quantity)

# approximation error issue whirl working with float
# roud() function should be used avoid it

sum_of_num = 1.23 + 2.80
print(sum_of_num)       # without a fix
print(round(sum_of_num, 2))       # rounding the result upto 2 decimal places

summed = 3.14159 + 2.71828
print(summed)
print(round(summed, 4))     # round upto 4 decimal place
