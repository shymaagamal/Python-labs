from   validation import *
from helper import *
import pwinput

# =====================================================================
#                       Authentication System:
# ========================================================================


# =====================================================================
#                       Registration Function
# ========================================================================

def Registration():
    userData={}
    fname = input("📝 Please enter your first name: ").strip()
    while not validate_name(fname): 
        fname = input("❌ Invalid input! First name must start with a letter:  ")

    lname = input("📝 Please enter your last name: ").strip()
    while not validate_name(lname):
        print("❌ Invalid input! Last name must start with a letter.")
        lname = input("Plese Enter a valid last name: ")

    name =fname+' '+lname
    userData["fullname"]=name

    email = input("📧 Please enter your email: ")
    while not validate_email(email):
        print("❌ Invalid email format! Example: user@example.com")
        email = input("Please enter a valid email: ").strip()
    
    exists,_=isUserExist(email)
    if  exists:
        print(f"\n\n❌ Oops! The email 📧 {email} is already registered. Try another one! 😊\n\n")
        return False,None
    
    userData["email"]=email
    

    mobilePhone = input("📱 Please enter your mobile number (Egyptian format) ")
    while not validate_egyptian_phone(mobilePhone):
        print("❌ Invalid mobile number! Must start with 010, 011, 012, or 015 and contain 11 digits.")
        mobilePhone = input("Enter a valid mobileNumber: ").strip()
    
    userData["mobilePhone"]=mobilePhone

    password = pwinput.pwinput("🔑 Enter your password: ", mask="*")

    confirmPassword=pwinput.pwinput("🔒 Confirm your password: ", mask="*")
    while not check_password(password,confirmPassword):
        print("❌ Passwords do not match! Please try again.")
        password = pwinput.pwinput("🔑 Enter your password: ", mask="*")
        confirmPassword=pwinput.pwinput("🔒 Confirm your password: ", mask="*")
    
    
    hashedPassword=hash_password(password).decode() 
    userData["password"]=hashedPassword

    print("\n\n✅ Registration Successful! Welcome, " + userData["fullname"] + " 🎉\n\n")
    save_Data_inJsonFile(userData,"./Crowd-Funding-console-app/user_data.json")    
    return True,email


# =====================================================================
#                       Login Function
# ========================================================================

def Login():
    email = input("📧 Please enter your email: ")
    exists, userData = isUserExist(email)
    if  not exists:
        print(f"\n\n⚠️ Oops! The email 📧 '{email}' was not found in our records. 🔍 Please check and try again! 😊\n\n")
        return False,email
    password = pwinput.pwinput("🔑 Enter your password: ", mask="*")
    is_password_correct =check_hashedPassword(password,userData[0]["password"])
    if is_password_correct:
        return True,email
    print("\n\n❌ Incorrect password. Ensure you're entering the right one and try again.\n\n")
    return False, email

    
    
    


