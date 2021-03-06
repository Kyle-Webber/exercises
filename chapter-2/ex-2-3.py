# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats
acrenumber = 0.0
feet = float(0)


# Constant for the number of square feet in an acre.
SQUAREFOOT = 0.0000229568411 

# Get the square feet in the tract from the user.
# you will need to convert this input to a float
squarefeet = input("Enter the number of square feet: ")
squarefeet = float(squarefeet)

# Calculate the number of acres.
acres = squarefeet*SQUAREFOOT

# Print the number of acres.
# remember to format the acres to two decimal places
output = "The number of acres is %.5f. Good effort, mate." % acres
print(output)



