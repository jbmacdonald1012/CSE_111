#import date time 
from datetime import datetime

#Get subtotal from user
subtotal = float(input('Please enter the subtotal: '))

#Get current time and day of the week
day_of_week_now = datetime.now()
weekday = day_of_week_now.weekday()
#weekday = 5

#set discount amount and tax
discount = .10
sales_tax = .06

#Evaluate conditions of the discount
if subtotal >= 50 and (weekday == 1 or weekday == 2): 
    discount_amount = subtotal * discount
    subtotal = subtotal - discount_amount
    tax = subtotal * .06
    total_due = subtotal + tax
    print(f'Discount Amount: {discount_amount:.2f}')
    print(f'Sales tax amount: {tax:.2f}')
    print(f'Total: {total_due:.2f}')

elif subtotal < 50 and (weekday == 1 or weekday == 2) : 
    spend_for_discount = 50.00 - subtotal
    print(f'If you spend {spend_for_discount:.2f} you qualify for a discount')
    tax = subtotal * .06
    total_due = subtotal + tax
    print('Otherwise, it will be')
    print(f'Sales tax amount: {tax:.2f}')
    print(f'Total: {total_due:.2f}')

else:
    tax = subtotal * .06
    total_due = subtotal + tax
    print(f'Sales tax amount: {tax:.2f}')
    print(f'Total: {total_due:.2f}')
