# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats
length_a = 0.00
width_a = 0.00
area_a = 0.00
length_b = 0.00
width_b = 0.00
area_b = 0.00

# Get length A from the user and convert it to a float
a_length = input("Please enter length A. ")
a_length = float(a_length)

# Get width A from the user and convert it to a float
a_width = input("Please enter width A. ")
a_width = float(a_width)

# Get length B from the user and convert it to a float
b_length = input("Please enter length B. ")
b_length = float(b_length)

# Get width B from the user and convert it to a float
b_width = input("Please enter width B. ")
b_width = float(b_width)

# Calculate area A
a_area = a_length*a_width

# Calculate area B
b_area = b_length*b_width

# Print each area, formatting the values to 2 decimal places
output_area_a = "The area for rectangle A is %.2f." % a_area
output_area_b = "The area for rectangle B is %.2f." % b_area
print(output_area_a,output_area_b)

# if area A is greater, print "A is greater" message.
if a_area > b_area:
    print("A is greater than B.")
# else if area B is greater, print "B is greater" message.
elif b_area > a_area:
    print("B is greater than A.")
# else print "A and B are equal" message.
elif a_area == b_area:
    print("A and B are equal.")

