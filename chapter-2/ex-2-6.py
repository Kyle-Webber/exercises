# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats
purchaseamount = 0.00
statetax = 0.00
countytax = 0.00
totaltax = 0.00
totalsale = 0.00

# Constants for the state and county tax rates
staterate = .06
countyrate = .06

# Get the amount of purchase from the user, casting it to a float.
purchase_amount = input("Enter the dollar amount of purchase: ")
purchase_amount = float(purchase_amount)

# Calculate the state sales tax.
statesalestax = purchase_amount*staterate

# Calculate the county sales tax.
countysalestax = purchase_amount*countyrate

# Sum the total tax.
total_tax = statesalestax+countysalestax

# Calculate the total of the sale.
totalamount = purchase_amount+total_tax

# Print detailed information about the sale, formatting all values to two decimal places.
output = "Your total before taxes is %.2f." % purchase_amount
output1 = "Your total for state sales tax is %.2f." % statesalestax
output2 = "Your total for county sales tax is %.2f." % countysalestax
output3 = "Your total tax for the purchase is %.2f." % total_tax
output4 = "Your total overall is %.2f." % totalamount
print(output,output1,output2,output3,output4)




