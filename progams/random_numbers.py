import random
import math

quantity = 1
def main():
    '''Has no parameters'''
    #Creates a list named numbers

    numbers_list = [16.2, 75.1, 52.3]
    print (numbers_list)
    # Calls the append_random_numbers function with only one argument to add one number to numbers
    append_random_numbers(numbers_list)
    print (numbers_list)
    # Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    append_random_numbers(numbers_list, 3)
    print (numbers_list)


    words = []
    
    append_random_words(words)
    print (words)
    
    append_random_words(words,4)
    print (words)



def append_random_numbers(numbers_list, quantity =1):
    '''Has two parameters: a list named numbers_list and an integer named quantity. The parameter quantity has a default value of 1'''
    # Computes quantity pseudo random numbers by calling the random.uniform function.
    # quantity_random = random.uniform(1, 100)


    # Rounds the quantity pseudo random numbers to one digit after the decimal.

    # Appends the quantity pseudo random numbers onto the end of the numbers_list.
    for i in range(quantity):
        quantity_random = random.uniform(1, 100)
        quantity_random = round(quantity_random, 1)
        numbers_list.append(quantity_random)

def append_random_words(words_list, quantity =1):
    '''Has two parameters: a list named numbers_list and an integer named quantity. The parameter quantity has a default value of 1'''

    words_choice =['dog', 'bear', 'goose', 'duck', 'bug', 'cat', 'translucent']
    # Computes quantity pseudo random numbers by calling the random.uniform function.
    # quantity_random = random.uniform(1, 100)


    # Rounds the quantity pseudo random numbers to one digit after the decimal.

    # Appends the quantity pseudo random numbers onto the end of the numbers_list.
    for i in range(quantity):
        quantity_random = random.choice(words_choice)
        
        words_list.append(quantity_random)

if __name__ == '__main__':
    main()








