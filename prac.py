# a = 3
# print(a)

# name = "Wakil"
# txt = "My name is {}"
# print(txt.format(name))

# price = 45
# txt = "The price is {} dollals"
# print(txt.format(price))

# price = 45
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))

# quatity = 456
# product = "clothes"
# price = 50
# my_order = "I need {} pieces of {} for {:.2f} dollars"
# print(my_order.format(quatity, product, price))


# quatity = 456
# product = "clothes"
# price = 50
# my_order = "I need {0} pieces of {1} for {2} dollars"
# print(my_order.format(quatity, product, price))

# quatity = 456
# product = "clothes"
# price = 50
# my_order = "I need {0} pieces of {1} for {2:.2f} dollars"
# print(my_order.format(quatity, product, price))

# #string Interpolation
# name = "Alice"
# age = 30 
# message = f"My name is {name} and I am {age} years old."
# print(message)

# #str.format() method
# name = "Alice"
# age = 30
# print("My name is {} and I am {} years old.".format(name, age))

# #Old-Style String Formatting ( % Operator)
# name = "Alice"
# age = 30
# message = "My name is %s and I am %d years old." % (name, age)


# name = input("Enter your name: ")
# age = input("Enter your age: ")
# email_msg = f"Hello {name}, you are {age} years old."
# print(email_msg)


# # A simple todo -list app

# # create an empty todo list


# a = [2, 5, 3, 4]
# a[2:2]=[2]
# print(a)

# lis = [[8,7], [6,5]]
# for p, q in lis:
#     print(p + q, end="&")

# s = "clcoding"
# x = slice(1, 4)
# print(s[x])

nums = [42, 8, 3, 17, 8]
nums.remove(8)
nums.sort()
print(nums)
print(''.join(str(nums)[1:-1]))