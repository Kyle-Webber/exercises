# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.
age_cat_1 = 0
age_cat_1 = int(age_cat_1)
age_cat_2 = 0
age_cat_2 = int(age_cat_2)
age_cat_3 = 0
age_cat_3 = int(age_cat_3)
age_cat_4 = 0
age_cat_4 = int(age_cat_4)

# Get the person's age.
# remember to convert the input to an int.
age_input = input("Enter your age: ")
age_input = int(age_input)

# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.
def age_input(age):
    if age_input >= 1:
     age = "Infant"
    elif age_input >= 12:
     age = "Child"
    elif age_input >= 19:
     age = "Teenager"
    elif age_input < 19:
     age = "Adult"
  
# display a message with the age category.
print("You are a(n) %f") % age

