# Assignment 1

# Question
'''
Write a program that converts temperature in celsius to fahrenheit.
The program should prompt the user for the temperature value
'''

# Solution
#Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 1.835) + 32

# Result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit ")


# Assignment 2

# Question 1
'''
You're building a program to determine the cost of a trip. The user provides the distance of the trip 
in miles, and you need to determine the cost of the trip based on the ffg criteria:
Distance <= 100 miles: $5
Distance > 100 miles and <= 500 miles: $8
Distance > 500 miles: $10
'''

# Solution 1
Distance = float(input("Enter the distance of your trip in miles: "))
if Distance <= 100:
    print("The cost of your trip is $5")
elif Distance <=500:
    print("The cost of your trip is $8")
else:
    print("The cost of your trip is $10")


# Question 2
'''
You're developing a program for a movie theater to calculate ticket prices.
The user enters their age and the movie time (Morning, afternoon or evening).
The tickect prices are as follows:
- Morning shows are #100 for all ages.
- Afternoon shows are #150 for adults (18 and above) and #100 for children.
- Evening shows are #200 for adults and #100 for children.
Write a program to calculte and display the ticket price.
'''

# Solution 2
Age = int(input("Enter your age: "))
Movie_Time = input("Enter the move time: (morning, afternoon or evening): ").lower()
if Movie_Time == "morning":
    print("The cost of your movie cost is #100")

elif Movie_Time == "afternoon" and Age >= 18:
    print("You're an adult, your movie cost is #150")
elif Movie_Time == "evening" and Age >= 18:
    print("You're an adult, your movie cost is #200")
else:
    print("You're a children, your movie cost is #100 ")






