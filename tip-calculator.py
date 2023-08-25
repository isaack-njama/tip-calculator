# /usr/bin/bash

"""
Requirements:
1. Ask the user to enter the charge for food
2. Calculate the amounts of:
    - an 18% tip and
    - 7% sales tax on charge of food
3. Display each of these amounts
4. Add everything and display the charge of food plus tip and sales tax
"""


def tip_calculator(tip_percent, sales_tax):
    base_charge = float(input("Please enter the charge for your meal in KES: "))

    tip_amount = base_charge * tip_percent
    sales_tax_amount = base_charge * sales_tax
    net_charge = base_charge + (tip_amount + sales_tax_amount)

    print("The expected tip amount is: {0:.2f} KES".format(tip_amount))
    print("The expected amount from sales is: {0:.2f} KES".format(sales_tax_amount))
    print("The total amount on your meal is: {0:.2f} KES".format(net_charge))

    return tip_amount, sales_tax_amount, net_charge


res = tip_calculator(0.18, 0.07)
print(res)
