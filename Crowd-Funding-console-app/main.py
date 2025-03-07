from authentication import *
from project_controller import *
from user_project_dashboard import *
# =====================================================================
#                       Crowd-Funding Console App
# ========================================================================

def main_menu():
    print("💡 Welcome to the 🚀 Crowd-Funding App! 💰")
    print("📌 1️⃣  Login")
    print("📌 2️⃣  Sign Up")
    print("📌 3️⃣  Exit")

    choice = input("Please enter your choice (1/2/3): ")


    if choice == "1":
        print("You chose to log in.")
        loggedin,email=Login()
        if not loggedin:
            main_menu()
        else:
            user_project_dashboard(email)

    elif choice == "2":
        print("You chose to sign up.")
        registred,email=Registration()
        if not registred:
            main_menu()
        else:
            post_registration_menu(email)      

            
    elif choice == "3":
        print("\n\n👋 Exiting the application... Goodbye! 🚀\n\n")
        exit()
    else:
        print("\n\n❌ Invalid choice! Please enter a valid option: 1️⃣ , 2️⃣ , or 3️⃣ .\n\n")
        main_menu()  

main_menu()    


