"""Python workbook Exercise 11: Fuel Efficiency

In the United States, fuel efficiency for vehicles is normally expressed
in miles-per-gallon(MPG). In Canada, fuel efficiency is normally expressed
in liters-per-hundred kilometers (L/100 km). Use your research skills to
determine how to convert from MPGto L/100 km. Then create a program that
reads a value from the user in American units and displays the equivalent
fuel efficiency in Canadian units.

"""

def mpg_lkm(mpg=None):
    L_per_gallon = 3.78541
    miles_per_100km = 62.15
    MPG_per_100L_Km = (miles_per_100km * L_per_gallon) / mpg
    return(MPG_per_100L_Km)





