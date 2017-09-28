# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.
price1 = 0.00
price2 = 0.00
price3 = 0.00
price4 = 0.00
price5 = 0.00

subtotal = 0.00
total = 0.00

prices = float(0)
# Constant for the sales tax rate.
tax_rate = .07

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.
priceuno = input("Enter the first price: ")
priceuno = float(priceuno)

pricedos = input("Enter the second price: ")
pricedos = float(pricedos)

pricetres = input("Enter the third price: ")
pricetres = float(pricetres)

pricecuatro = input("Enter the fourth price: ")
pricecuatro = float(pricecuatro)

pricecinco = input("Enter the fifth price: ")
pricecinco = float(pricecinco)

# Calculate the subtotal by adding up the item prices.
subtotal_amount = priceuno+pricedos+pricetres+pricecuatro+pricecinco

# Calculate the sales tax by multiplying the subtotal by the tax rate.
sales_tax = subtotal_amount*tax_rate

# Calculate the total by adding the subtotal and tax.
total = subtotal_amount+sales_tax

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 
output = "Your subtotal today will be %.2f." % subtotal_amount 
output1 = "The tax for this transaction will be %.2f." % sales_tax
output2 = "Your total today will be %.2f." % total
print(output,output1,output2)




