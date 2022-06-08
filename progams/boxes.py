#import math to use math methods
import math

# Get the input from the user for the number of items and items per box
items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

#calculate
solution = math.ceil(items/items_per_box)

print(f'For {items} items, packing {items_per_box} items in each box, you will need {solution} boxes.')