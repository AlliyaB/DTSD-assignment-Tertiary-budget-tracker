"""Import date and datetime."""
from datetime import datetime
from datetime import date

# Print todays date.
today = date.today()
d = today.strftime("%d/%m/%y")
print(f"Date: {d}")

def calculate_age(birth_date: datetime) -> int:
    """Function to carry out age calculation based off birthdate 
    (dd/mm/yyyy).
    """
    # Get today's date.
    today: date = date.today()
    # Calculate the year difference between today and the date of birth.
    difference: int = today.year - birth_date.year
    # Find out if today preceeds the date of birth this year.
    today_preceeds_DOB: int = int((today.month, today.day) <
                                  (birth_date.month, birth_date.day))
    age: int = difference - today_preceeds_DOB
    return age

# Validating the users age.    
invalid = True
while invalid:
    try:
        birth_date_str: str = input("Please enter your birth date " +
                                    "(dd/mm/yyyy): ")
        # Validate user input to ensure it is in the format dd/mm/yyyy.
        birth_date: datetime = datetime.strptime(birth_date_str,
                                                    '%d/%m/%Y')

    except ValueError as err:
        # Display a nice error message.
        if str(err) == "Day is out of range for month.":
            print(err)
        else:
            print(f"'{birth_date_str}' is not in the format " +
                    "dd/mm/yyyy")
            
    else:
        # Calculate the user's age.
        age: int = calculate_age(birth_date)
        if age >=18 and age <= 99:
            print(f"You are {age} years old.\n")
            break
        else:
            if age <= 0:
                print("This birthdate is invalid")
            elif age <= 18:
                print(f"You are {age} years old. ")
                exit()

            elif age >= 99:
                print(f"You are {age} years old.")
                exit()
    
else:
    invalid = False