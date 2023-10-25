# Assignment 1

# Question
'''
Write a program that converts temperature in celsius to fahrenheit.
The program should prompt the user for the temperature value
'''

# Solution
#Input temperature in Celsius
# celsius = float(input("Enter temperature in Celsius: "))

# # Convert Celsius to Fahrenheit
# fahrenheit = (celsius * 1.835) + 32

# # Result
# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit ")


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
# Distance = float(input("Enter the distance of your trip in miles: "))
# if Distance <= 100:
#     print("The cost of your trip is $5")
# elif Distance <=500:
#     print("The cost of your trip is $8")
# else:
#     print("The cost of your trip is $10")


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
# Age = int(input("Enter your age: "))
# Movie_Time = input("Enter the move time: (morning, afternoon or evening): ").lower()
# if Movie_Time == "morning":
#     print("The cost of your movie cost is #100")

# elif Movie_Time == "afternoon" and Age >= 18:
#     print("You're an adult, your movie cost is #150")
# elif Movie_Time == "evening" and Age >= 18:
#     print("You're an adult, your movie cost is #200")
# else:
#     print("You're a children, your movie cost is #100 ")






# Assignment 3

# Union
'''
union of two sets creates a new set that contains all the distinct elements from both sets,
without any duplicates.
''' 
# Example 1
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# union_set = set1.union(set2)

# print(union_set)


# Example 2

# setA = {1, 2, 3}
# setB = {3, 4, 5}

# union_set = setA | setB

# print(union_set)


# Intersection
'''
It returns a new set containing all the elements that are present in all of the input sets.
'''

# Example 1

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6}

# intersection_set = set1.intersection(set2)

# print(intersection_set)

# Example 2

# setA = {1, 2, 3, 4, 5}
# setB = {3, 4, 5, 6}

# intersection_set = setA & setB

# print(intersection_set)


# intersection update
'''
intersection update is used to update a set by keeping only the elements 
that are common to the set and one or more other sets.
'''

# Example 1
# set1 = {1, 2, "book", 4, 5}
# set2 = {"book", 4, 5, 6}

# set1.intersection_update(set2)

# print(set1)

# Example 2 
# setA = {"people","food", "education", 9}
# setB = {"girl", "boy", "food", 5, 9, "people"}

# setB.intersection_update(setA)
# print(setB)


# symmetric difference
'''
symmetric difference is used to find the elements that are unique to each of the input sets 
while excluding elements that are common to both sets.
'''
# Example 1
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6}

# sym_diff_set = set1.symmetric_difference(set2)

# print(sym_diff_set)

# Example 2
# setA = {1, 2, 3, 4, 5}
# setB = {3, 4, 5, 6}

# sym_diff_set = setA ^ setB

# print(sym_diff_set)


# symmetric difference update
'''
symmetric difference update is used to update a set by keeping only the elements that are unique 
to the set and one or more other sets, while excluding elements that are common to both sets. 
'''
# Example 1
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6}

# set1.symmetric_difference_update(set2)

# print(set1)

# Example 2
# setA = {1, 2, "phone", 4, 5, "house"}
# setB = {3, 4, 5, "house"}

# setB.symmetric_difference_update(setA)

# print(setB)


# Difference
'''
difference is used to find the elements that are unique to one set, 
excluding elements that are present in another set.
'''
# Example 1
# set1 ={1, "good", 3, 9, 4, 5}
# set2 = {3, 4, 5, 6, "come"}

# difference_set = set1.difference(set2)

# print(difference_set)


# Example 2
# setA = {1, "good", 3, 9, 4, 5}
# setB = {3, 4, 5, 6, "come"}

# difference_set = setA - setB

# print(difference_set)


# Difference Update
'''
difference update is used to update a set by removing elements that are also present in another set. 
'''
# Example 1
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6}

# set1.difference_update(set2)

# print(set1)

# # Example 2 
# set1 = {"apple", 2, 3, 4, "banana"}
# set2 = {3, 4, 5, "orange"}

# set1.difference_update(set2)

# print(set1)


# Issubset
'''
issubset is used to check if one set is a subset of another set. 
A subset is a set that contains only elements that are also present in the other set.
'''
# Example 1
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}

# # Check if set1 is a subset of set2
# is_subset = set1.issubset(set2)

# print(is_subset)

# # Example 2
# setA = {"power", 2, 3}
# setB = {1, 2, 3, 4, 5}

# # Check if set1 is a subset of set2
# is_subset = setA.issubset(setB)

# print(is_subset)


# set1 = {"power", 2, 3}
# set2 = {1, 2, 3, 4, 5}

# # Check if set1 is a subset of set2
# is_subset = set1 <= set2

# print(is_subset)


# Issuperset
'''
issuperset is used to check if one set is a superset of another set. 
A superset is a set that contains all the elements of another set.
'''

# Example 1
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4}

# # Check if set1 is a superset of set2
# is_superset = set1.issuperset(set2)

# print(is_superset)

# Example 2
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4}

# # Check if set1 is a superset of set2
# is_superset = set1 <= set2

# print(is_superset)


# Isdisjoint
'''
isdisjoint is used to determine whether two sets are disjoint, 
which means they have no elements in common.
'''
# Example 1
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# Check if set1 and set2 are disjoint
is_disjoint = set1.isdisjoint(set2)

print(is_disjoint)

# Example 2
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Check if set1 and set2 are disjoint
is_disjoint = set1.isdisjoint(set2)

print(is_disjoint)