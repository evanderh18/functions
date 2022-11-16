# Conversion Calculator
# By: Evan VanderHoeven

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user

user_number = float(input("What number to convert? "))
user_unit = input("What unit is your number?" )

if(user_unit == 'in'):
    #perform in to mm
    converted_number = user_number * 25.4
    conv_unit = 'mm'
if(user_unit == 'mm'):
    #performmm to in
    converted_number = user_number / 25.4
    conv_unit = 'in'
else:
    print('That is not a valid unit')
print(converted_number, conv_unit)