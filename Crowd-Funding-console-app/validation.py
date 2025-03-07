import re
from datetime import datetime
def validate_name(name): 
    name_regex = re.compile(r"^[a-zA-Z].*")
    if name_regex.match(name):
            return True
    else:
            return False

def validate_email(email): 
    email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$")
    if email_regex.match(email):
            return True
    else:
            return False

            
def check_password(password,confirmedPassword):
       if password != confirmedPassword :
              return False
       return True

import re


def validate_egyptian_phone(phone):
    egypt_phone_regex = re.compile(r"^(010|011|012|015)\d{8}$")
    if egypt_phone_regex.match(phone):
        print("Valid Egyptian phone number!")
        return True
    else:
        print("Invalid phone number! Must start with 010, 011, 012, or 015 and have 11 digits.")
        return False


def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")  
    except ValueError:
        return None  

def get_valid_date(message):
    while True:
        date_str = input(message).strip()  
        date = validate_date(date_str)
        if date:
            return date  
        print("❌ Invalid date format! Please enter in YYYY-MM-DD.")



