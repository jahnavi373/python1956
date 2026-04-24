# Representbelow data in python
# Variables
brand_name = 'United Colors of Benetton'
product_desc = "Mn Spread Collar Checked cotton Casual Shirt"
product_rating = 3.8
product_price = 1651
product_sizes = [38,40,42]
print(type(product_sizes))

x = "python"
y = " is"
z = " awesome"
print(x+y+z) 

x = 10
y = 20
print(x+y)
z = " awesome"
# print(x+z) --> TypeError: unsupported operand type(s) for +: 'int' and 'str'
# wanted to print string and number
print(x,z)

x,y,z = "one","two","three"
print(x,y,z)

#x,y,z = "one","two","three","four" --> ValueError: too many values to unpack (expected 3, got 4)
#print(x,y,z)

x = y = z = "One"
print(x)
print(y)
print(z)