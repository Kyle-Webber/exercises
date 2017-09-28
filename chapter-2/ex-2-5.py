# Programming Exercise 2-5
#
# Program to calculate distances traveled over time at a speed.
# This program uses no input.
# It will calculate the distance traveled for 6, 10 and 15 hours at a constant speed,
# then display all the results on the screen.

# Variables to hold the three distances.
# be sure to initialize these as floats.
time1 = 6
time2 = 10
time3 = 15

distances = float(0)

# Constant for the speed.

speed = 55

# Calculate the distance the car will travel in
# 6, 10, and 15 hours.

trip1 = time1*speed
trip2 = time2*speed
trip3 = time3*speed


# Print the results for all calculations.

output = "The distance traveled in 6 hours, going 55 mph, is %d." % trip1
output1 = "The distance traveled in 10 hours, going 55 mph, is %d." % trip2
output2 = "The distance traveled in 15 hours, going 55 mph, is %d." % trip3
print(output,output1,output2)
