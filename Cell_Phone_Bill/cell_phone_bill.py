"""
A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.


Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places
"""

base_charge = 15
emergency_support = 0.44
extra_min = 0.25
extra_text = 0.15

def cell_phone_bill(total_minutes, total_texts):
    additional_minutes = 0
    additional_texts = 0
    additional_minutes += (total_minutes - 50) * extra_min
    additional_texts += (total_texts - 50) * extra_text
    subtotal = base_charge + emergency_support
    tax = 0.05 * subtotal

    result = f"{'Monthly rate:':25} {base_charge:.2f}\n"\
          f"{'Emergency support:':25} {emergency_support:.2f}\n"
    if additional_minutes > 0:
        subtotal += additional_minutes
        result += f"{'Additional minutes:':25} {additional_minutes:.2f}\n"
    if additional_texts > 0:
        subtotal += additional_texts
        result += f"{'Additional texts:':25} {additional_texts:.2f}\n"
    total = subtotal * 1 + tax
    result += f"{'Tax:':25} {tax:.2f}\n{'Total:':25} {total:.2f}"
    return result


