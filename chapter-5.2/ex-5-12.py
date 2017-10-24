# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function
def main():
    # Define local variables to hold two integers
    integer1 = 0
    integer2 = 0

    # prompt the user for the first integer
    integer1 = int(input("Enter the first integer: "))
    
    # prompt the user for the second integer
    integer2 = int(input("Enter the second integer: "))

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    this_one = compare_integers(integer1, integer2)
    print(this_one)
    
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def compare_integers(integer1,integer2):
	# if the first integer is greater, return the first integer
    if integer1 > integer2:
       print("Integer 1 is greater than 2.")
       return integer1
	# else, return the second integer
    elif integer2 > integer1:
       print("Integer 2 is greater than 1.")
       return integer2
    
print(compare_integers)
# Call the main function to start the program
main()