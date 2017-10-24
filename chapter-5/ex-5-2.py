# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates
STATE_TAX = .06
COUNTY_TAX = .06
#Johnson county has no sales tax, so I won't include it in the rest of the calculation.


# define the main function
def main():
    print("Running Webster's Tax Calculator...")
    # Define local float variables for purchase, state tax and county tax
    amount = 0.0
    state_tax = 0.0
    county_tax = 0.0
    # Get the purchase amount from the user
    purchase = float(input("Enter the amount of your purchase: "))
    # Calculate the state tax using the global constant for state tax rate
    state_tax = purchase*STATE_TAX
    # Calculate the county tax using the global constant for county tax rate
    county_tax = purchase*COUNTY_TAX
    # Call the sale details function, passing the purchase, state tax and county tax
    sales_details = (purchase, state_tax, county_tax)


# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details
def sales_details(purchase, state_tax, county_tax):
    # Define local float variables for total tax and sale total
    total_tax = 0.0
    sale_total = 0.0
	# Calculate the total tax
    total_tax = state_tax+county_tax
	# Calculate the total sale
    sale_total = total_tax + purchase
    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.
    print("Your total purchase today is",purchase,". Your state tax rate is",state_tax,". Your county sales tax rate is",county_tax,".")
    print("Your total tax is",total_tax,". Your sales total for today is",sale_total,".")

# Call the main function to start the program.
main()
