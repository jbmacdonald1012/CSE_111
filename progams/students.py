import csv

def main():
    
    INUMBER_INDEX = 0
    NAME_INDEX = 1

    student_dict = read_dict("students.csv", INUMBER_INDEX)

    inumber = (input('Please enter an I-Number (XXXXXXXXX): '))

    if not inumber.isdigit():
        print('Invalid character in I-Number')
    
    if len(inumber) < 9:
       print("Invalid I-Number: too few digits")
    
    if len(inumber) > 9:
        print("Invalid I-Number: too many digits")
    
    if inumber not in student_dict:
        print('No such student')
    
    value = student_dict[inumber]
    name = value[NAME_INDEX]
    print(name)


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
 
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
 
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
 
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
 
        # The first row of the CSV file contains column
        # headings and not the data we want to use,
        # so this statement skips the first row of the CSV file.
        next(reader)
 
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
 
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]
 
            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list
 
    # Return the dictionary.
    return dictionary


if __name__ == "__main__":
    main()