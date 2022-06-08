#Import math to use math.pi
import math
from datetime import datetime

#Get inputs from the user and convert from string to number. 
width = float(input('Enter the width of the tire in mm (ex 205): '))
aRatio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of wheel in inches (ex 15): '))

#calculate the volume of air in liters
volume = math.pi * width ** 2 * aRatio * (2540 * diameter + width * aRatio)
volumeLiters = volume / 10000000000

#Round the volumen to 2 decimal places
volumeLiters = round(volumeLiters, 2)

print (f'The approximate volume is {volumeLiters}')
print()

current_date = datetime.now()
purchaseTires = input('Would you like to purchase these tires? ')

print()
if purchaseTires == 'Yes':
    phoneNumber = input('Please enter your phone number: ')
    with open('volumes.txt','at') as volume_file:
        print(f'{current_date:%Y-%m-%d}, {width}, {aRatio}, {diameter}, {volumeLiters}, {phoneNumber}', file=volume_file)
else:
    with open('volumes.txt','at') as volume_file:
        print(f'{current_date:%Y-%m-%d}, {width}, {aRatio}, {diameter}, {volumeLiters}', file=volume_file)