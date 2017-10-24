# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed



# Global constant for the percent of replacement cost to insure
REPLACEMENT_COST_CONSTANT = .8


# Define the main function
def main():
    # Define local float variables for replacement cost and minimum insurance
    replacement_cost = 0.0
    minimum_insurance = 0.0

    # Get the replacement cost from the user
    replacement_cost = float(input("Enter the replacement cost of your item: "))
    # Calculate the minimum insurance amount using the global constant
    minimum_insurance = replacement_cost*REPLACEMENT_COST_CONSTANT
    # Call the function to display the insurance details, 
    # passing the replacement cost and minimum insurance to the function
    insurance_details(replacement_cost, minimum_insurance)

      
# Define a function to display the insurance details
# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.
def insurance_details(replacement_cost, minimum_insurance):
    replacement_cost = 0.0
    minimum_insurance = 0.0   
	# display the replacement cost, formatting the value to 2 decimal places
    formatted_replacement = format(replacement_cost,'.2f') 
    print("The replacement cost for your item is",formatted_replacement,".")
    # display the percent insured, formatting the value to 2 decimal places
    print("The percent you are insured is",REPLACEMENT_COST_CONSTANT," or 80%.")
	# display the minimum insurance, formatting the value to 2 decimal places
    formatted_minimum = format(minimum_insurance,'.2f')
    print("The minimum insurance you need is",formatted_minimum,".")

# Call the main function to start the program
main()
