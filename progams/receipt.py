import csv
from datetime import datetime


def main():
    try:    
        PRODUCT_NUMBER_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2

        products_dict = read_dict('products.csv', PRODUCT_NUMBER_INDEX)

        print('Star Market')
        print()
        shoppinglist()
        print()
        print('Thank you for choosing Star Market')
        print()
        #Add DateTime here
        #Format = 3 char wd, 3 char month, single digit date (if applicable)
        # HH : MM : SS, 4 char year
        current_time = datetime.now()
        print(f'{current_time: %c}')
    
    except KeyError as key_error:
        print(f'{key_error} That item is unavailable at Star Market')
    except FileNotFoundError as missing:
        print(f'{missing} : The file is missing')

def shoppinglist():
    
    PRODUCT_NUMBER_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2

    products_dict = read_dict('products.csv', PRODUCT_NUMBER_INDEX)

    #run through request CSV print results
    with open("request.csv", "rt") as request_file:
        
        reader = csv.reader(request_file)

        next(reader)

        number_of_items = 0
        subtotal = 0
        tax = 0.06

        for row_list in reader:
            product_number = row_list[PRODUCT_NUMBER_INDEX]
            quantity = row_list[PRODUCT_NAME_INDEX]


            value = products_dict[product_number]

            name = value[PRODUCT_NAME_INDEX]
            price = value[PRODUCT_PRICE_INDEX]

            print(f'{name}: {quantity} @ {price}')
            number_of_items += int(quantity)
            subtotal += float(quantity) * float(price)

    sales_tax = subtotal * tax
    total = subtotal + sales_tax
    print()
    print(f'Number of Items: {number_of_items}')
    print(f'Subtotal: {subtotal:.2f}')
    print(f'Sales Tax: {sales_tax:.2f}')
    print(f'Total: {total:.2f}')


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]

            dictionary[key] = row_list

    return dictionary



if __name__ == '__main__':
    main()
