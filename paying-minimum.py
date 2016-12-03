"""
edX MITx 6001x, "Introduction to Computer Science with Python"

Problem Set 2

Problem 1: Paying the Minimum (10 points possible)
--------------------------------------------------

Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each
month.

The following variables contain values as described below:
  balance - the outstanding balance on the credit card
  annualInterestRate - annual interest rate as a decimal
  monthlyPaymentRate - minimum monthly payment rate as a decimal*

*(...a credit card statement will come with the option for you to pay
a minimum amount of your charge, usually 2% of the balance due).

For each month, calculate statements on the monthly payment and remaining
balance, and print to screen something of the format:
  Month: 1
  Minimum monthly payment: 96.0
  Remaining balance: 4784.0

Be sure to print out no more than two decimal digits of accuracy - so print
Remaining balance: 813.41 instead of Remaining balance: 813.4141998135 

Finally, print out the total amount paid that year and the remaining balance
at the end of the year in the format:
  Total paid: 96.0
  Remaining balance: 4784.0

A summary of the required math is found below:
  Monthly interest rate= (Annual interest rate) / 12.0
  Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)  
  Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
  Outstanding balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Hints
Only two decimal digits of accuracy?? Use the `round()` function!

How to think about this problem?
To help you get started, here is a rough outline of the stages you could
follow when writing your code:
  For each month:
    Compute the monthly payment, based on the previous month’s balance.
    (i.e., it's a fraction of the balance)
    Update the outstanding balance by deducting the payment, then charging
    interest on the result.
    Output the month, the minimum monthly payment and the remaining
    outstanding balance.
    Keep track of the total amount of paid over all the past months so far.
  Print out the result statement with the total amount paid and the remaining
  balance.

Use these ideas to guide the creation of your code.
"""

# Prompt for input
print("Omit dollar signs and percentage signs when entering numbers.\n")
balance = input("Enter current total balance: ").strip()
apr = input("Enter the annual interest rate: ").strip()
min_pmt = input("Enter the card's minimum monthly payment: ").strip()


# Check validity of inputs, correct if necessary, and convert to numeric
if '$' in balance:
    balance = float(balance.replace('$', '').strip())
else:
    balance = float(balance)

if '%' in apr:
    apr = float(apr.replace('%', '').strip())
else:
    apr = float(apr)
    if apr >= 1:  # make decimal if it was whole number
        apr /= 100

if '$' in min_pmt:
    min_pmt = float(min_pmt.replace('$', '').strip())
else:
    min_pmt = float(min_pmt)


# Variables for doing the calculations
monthly_pmt_rate = min_pmt / balance
monthly_int = apr / 12.0
totalPaid = 0.0


# Calculate the minimum payment
for m in range(12):  
    # Compute monthly payment based on previous balance
    min_pmt = monthly_pmt_rate * balance  
    # Update outstanding balance by subtracting the payment
    balance -= min_pmt
    # Charge interest on the updated balance
    balance += monthly_int * balance
    # Keep track of the total amount paid so far
    totalPaid += min_pmt     
    print("Month: {}".format(m+1))
    print("Minimum monthly payment: " + str(round(min_pmt, 2)))
    #print("Remaining balance: " + str(round(balance, 2)) + "\n")


# Output
print( "Total paid: ${}".format(round(totalPaid, 2)) )
print( "Remaining balance: ${}".format(round(balance, 2)) )
