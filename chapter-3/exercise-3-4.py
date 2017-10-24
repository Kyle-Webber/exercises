# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.
arabic_1 = 0
roman_1 = 0
arabic_2 = 0
roman_2 = 0
arabic_3 = 0
roman_3 = 0
arabic_4 = 0
roman_4 = 0
arabic_5 = 0
roman_5 = 0
arabic_6 = 0
roman_6 = 0
arabic_7 = 0
roman_7 = 0
arabic_8 = 0
roman_8 = 0
arabic_9 = 0
roman_9 = 0
arabic_10 = 0
roman_10 = 0

# Get number from user and convert it to an int
numeral = input("Please enter a number 1-10 to convert to a Roman numeral: ")
numeral = int(numeral)

# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.
if numeral == 1:
    print("The Roman numeral for 1 is I.")
elif numeral == 2:
    print("The Roman numeral for 2 is II.")
elif numeral == 3:
    print("The Roman numeral for 3 is III.")
elif numeral == 4:
    print("The Roman numeral for 4 is IV.")
elif numeral == 5:
    print("The Roman numeral for 5 is V.")
elif numeral == 6:
    print("The Roman numeral for 6 is VI.")
elif numeral == 7:
    print("The Roman numeral for 7 is VII.")
elif numeral == 8:
    print("The Roman numeral for 8 is VIII.")
elif numeral == 9:
    print("The Roman numeral for 9 is IX.")
elif numeral == 10:
    print("The Roman numeral for 10 is X.")

# use a final else to display an error if number is out of range.
elif numeral < 10:
    print("O O F")
elif numeral > 1:
    print("O O F")

# display the numeral on the screen.






