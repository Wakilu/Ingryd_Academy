# Variable
'''
Variable allows the representation and manipulation of data.
'''

x = 10  # x is variable, 10 is value assigned
name = "Wakil" # name is variable, "Wakil" is value assigned.

# Result
print(x) # give 10
print(name) # give "Wakil"

# Data type
'''
A data type is a classification or category that specifies which kind of data an object can hold.
'''

#integer
a = 42
print(a, type(a))

#float
a = 30.5
print(a, type(a))

#complex
a = 2 + 3j
print(a, type(a))

#string 
a = "Education"
print(a, type(a))

#list
a = [1, 3, 5, "come", "Done"]
print(a, type(a))

#tuple
a = (2, 4, 6, "Soon", "good")
print(a, type(a))

#dictionary
a = {"name":"Precios", "age": 34, "gender": "female"}
print(a, type(a))

#set
a = {3, 6, 9}
print(a, type(a))

#frozenset
a = frozenset([4, 6, 8, 10])
print(a, type(a))

#boolean (True or False)
x = 30
y = 50
a = x > y
print(a, type(a))

#none
a = None
print(a, type(a))

#bytes
a = b'\x48\x65\x6c\x6c\x6f'
print(a, type(a))

#bytearray
a = bytearray([65, 66, 67])
print(a, type(a))

#Array 


Product = input("Enter the product name: ")
Quantity = input(float("Enter the quantity of product sold: "))
Total_sale = Product * Quantity 
print("Product")
print(Quantity)
#print(f"Total sales amount is #{:.2f}".format{Total_sale}) 
