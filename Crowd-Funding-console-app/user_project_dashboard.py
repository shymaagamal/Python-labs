
from project_controller import *
from helper import clear_console

# =====================================================================
#                       Projects Dashboard
# ========================================================================

menu_actions={
    "1": create_userproject,
    "2": Edit_userProject,
    "3": view_UserProjects,
    "4": delete_UserProjects,
    "5": remove_project_by_title,
    "6":exit

}

def user_project_dashboard(email):
    clear_console()
    print("\n📂 **Project Management Menu**\n")
    print("🔹 1️⃣  Add a New Project")
    print("🔹 2️⃣  Edit an Existing Project")
    print("🔹 3️⃣  View Your Projects")
    print("🔹 4️⃣  Delete All Projects")
    print("🔹 5️⃣  Delete a Project")
    print("🔹 6️⃣  Exit")

    choice = input("📌 Enter your choice (🔢 1 to 6): ").strip()
    if choice in menu_actions and choice != "6":
        menu_actions[choice](email)
    elif choice == "6": 
        menu_actions[choice]()

    else:
        print("❌ Invalid choice! Please enter 1 or 6.")




def post_registration_menu(email):
    clear_console()
    print("\n🎉 **Welcome to the Crowd-Funding App!** 🚀")
    print("===========================================")
    print("📌 1️⃣  Go to **Your Project Dashboard** 🏗️")
    print("📌 2️⃣  Exit the Application ❌")
    print("===========================================")
    choice = input("📢 Please enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        user_project_dashboard(email)  
    elif choice == "2":
        print("\n👋 Thank you for using the Crowd-Funding App! See you soon. 🚀")
        exit()
    else:
        print("\n❌ Invalid choice! Please enter 1 or 2.")
        post_registration_menu(email) 