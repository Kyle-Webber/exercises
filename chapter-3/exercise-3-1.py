# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6
sunday = 7

# Get the number for the day of the week.
# be sure to format the input as an int
day = input("Enter a number for the day of the week: ")

# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.
if day == 1:
    print("The day of the week is Monday. Better thaw out some L A S A G A for Garfielf.")
elif day == 2:
    print("The day of the week is Tuesday. Time to eat at Ruby Tuesday. Get it, because Tuesday is in the name. haha")
elif day == 3:
    print("The day of the week is Wednesday. HUMP DAYYYYYYYY!")
elif day == 4:
    print("The day of the week is Thursday. Time to go to work to perform soul-crushing labour.")
elif day == 5:
    print("The day of the week is Friday. Time to party!!!!")
elif day == 6:
    print("The day of the week is Saturday. Time to watch the Hawkeyes play. If you prefer Iowa State, I'm gonna have to ask you politely yet firmly to leave.")
elif day == 7:
    print("The day of the week is Sunday. Sundays suck because Chick-Fil-A is closed :(")
    
# use the final else to display an error message if the number is out of range.
if day < 1:
    day = int(day)
    print("That's not a valid number. Try again, idiot.")
if day > 7:
    day = int(day)
    print("That's not a valid number. Try again, idiot.")
# display the name of the day on the screen.




