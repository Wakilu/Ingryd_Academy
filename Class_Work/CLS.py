# Question 1
'''
You're building a program to generate a personalized email msg. The use provides their name and age. 
Write a program that takes these input and create an email msg in the following format:
Hello <name>, you are <age> years old.
'''

# Solution
name = input("Enter your name: ")
age = input("Enter your age: ")
email_msg= f"Hello {name}, you are {age} years old."
print(email_msg)


# Question 2
'''
You're developing a report generator. You have data about sales, including the product name, 
quatity sold, and total sales amount. Create a program that take s this data and generate a report 
in the following format:
Product: <Product name>
Quantity: <Quantity sold>
Total Sales: #<total sales amount> to 2 dp.
'''

# Solution
Product = input("Enter the product name: ")
Quantity = input("Enter the quantity of product sold: ")
Total_sale = float(input("Enter total sales: "))
report = f"Product: {Product}\n Qunatity:{Quantity}\n Total Sales: #{round(Total_sale, 2)}."
print(report)


# Question 3
'''
You're building a URL generator. The user provides a domain name and a path. 
Write a program that takes inputs and create a complete URL. Ensure the URL include "https://" at the
beginning.
https://www.codewell.com/Home/Login
'''

domain_name = input("Enter the domain name: ")
path = input("Enter the path: ")

# Check if the domain already starts with "https://"
if domain_name.startswith("https://"):
    url = domain_name + path
else:
    url= f"https://{domain_name}/{path}"
    print(url)
# Display the complete URL
    print("Complete URL:", url)