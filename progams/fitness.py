# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
import math


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('What is your gender (M/F)?: ')
    birth_str = input('Birthdate in following format (YYYY-MM-DD): ')
    pounds = float(input('What is your weight (pounds)? '))
    inches = float(input('What is your height (inches)? '))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    years = compute_age(birth_str)
    weight = round(kg_from_lb(pounds), 2)
    height = cm_from_in(inches)
    bmi = round(body_mass_index(weight, height), 1)
    bmr = round(basal_metabolic_rate(gender, weight, height, years), 0)

    # Print the results for the user to see.
    print(f'Age: {years}')
    print(f'Weight (kg): {weight}')
    print(f'Height (cm): {height}')
    print(f'BMI: {bmi}')
    print(f'BMR: {bmr}')

    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """

    weight = pounds * 0.45359237

    return weight


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """

    height = inches * 2.54

    return height


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height * height)
    return bmi


def basal_metabolic_rate(gender, weight, height, years):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """

    if (gender == 'F'):
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * years)
   

    elif (gender == 'M'):
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * years)
   
    else:
        print('You need to endter M or F')
    
    return bmr
    

# Call the main function so that
# this program will start executing.

main()