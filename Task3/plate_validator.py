import re

# Plates are required to start with at least two letters.
def validate_letters(plate):
    pattern = r'^[A-Za-z]{2,}'

    if re.match(pattern, plate):
        return True
    return False

# Numbers should only be used at the end of the plate.
def validate_numbers(plate):
    pattern = r'^[A-Za-z]{2}[A-Za-z]*[0-9]*$'

    if re.match(pattern, plate):
        return True
    return False

# Needs to contain a minimum of 2(letters or numbers) characters and a maximum of 6.
def validate_count(plate):
    pattern = r'^[A-Za-z0-9]{2,6}$'

    if re.match(pattern, plate):
        return True
    return False

# First number used must not be a '0'.No whitespace characters or punctuation marks are allowed.
def validate_characters(plate):
    pattern = r'^[A-Za-z][A-Za-z1-9]*$'
    if re.match(pattern, plate):
        return True
    return False

def is_plate_valid(plate):
    if validate_letters(plate) and validate_count(plate) and validate_characters(plate) and validate_numbers(plate):
        return True
    return False

if __name__ == "__main__":
    plate = input("Enter a plate: ")
    
    if is_plate_valid(plate):
        print("Valid plate!")
    else:
        print("Sorry, invalid plate")
