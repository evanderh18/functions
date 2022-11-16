# Conversion Calculator
# By: Evan VanderHoeven

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user

user_number = float(input("What number to convert? "))
user_unit = input("What unit is your number?" )

# to convert in to mm --> in x 25.4
# to convert mm to in --> mm / 25.4

# user gives in unit
#converted_number = user_number * 25.4
converted_number = user_number / 25.4
if(user_unit == 'in'):
    #perform in to mm
    converted_number = user_number * 25.4
if(user_unit == 'mm'):
    #performmm to in
    converted_number = user_number / 25.4
print(converted_number)
print(user_unit)