# This file is used to print the age and name of a user after they have entered 
# their details in the terminal.
'''
To ensure that the user enters their name and age in the terminal we use the 
input() function.
The input() function takes a string as an argument, which is the prompt that 
the user will see.
The input() function then returns the string that the user entered.
'''
name = input("Welcome to the age printer! What is your name?: ")
age = input("Welcome to the age printer!How old are you?:")

print(f"Hi {name}! You are {age} years old!")
