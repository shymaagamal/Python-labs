
import click
from   validation import get_valid_date
from helper import *
from datetime import datetime


# =====================================================================
#                       Create Project
# ========================================================================

def create_userproject(email):
    projectData={}
    projectData["email"]=email
    title = input("📝 Please enter project title: ").strip()
    isTitleExist= is_project_title_unique_for_user(email,title)
    while not isTitleExist:
        title = input("📝 Please enter another project title: ").strip()
        isTitleExist= is_project_title_unique_for_user(email,title)

    projectData["title"]=title

    detail = input("📝 Please enter project Details: ").strip()
    projectData["detail"]=detail

    totalTarget = click.prompt("📝 Please enter project total target", type=int)
    projectData["totalTartget"]=totalTarget
    start_date = get_valid_date("📅 Enter Project start date (YYYY-MM-DD): ")
    end_date = get_valid_date("📅 Enter Project end date (YYYY-MM-DD): ")

    while end_date <= start_date:
        print("⚠️ End date must be after the start date! Try again.")
        end_date = get_valid_date("📅 Enter project end date (YYYY-MM-DD): ")
    projectData["startDate"]=start_date.isoformat()
    projectData["endDate"]=end_date.isoformat()


    project_id=len(read_allData("./Crowd-Funding-console-app/users_projects.json"))+1
    projectData["id"]=project_id
    save_Data_inJsonFile(projectData,"./Crowd-Funding-console-app/users_projects.json")

# =====================================================================
#                       View Project
# ========================================================================
def view_UserProjects(email):
    allProjects=read_allData("./Crowd-Funding-console-app/users_projects.json")
    filteredProjects = list(filter(lambda project: project["email"] == email, allProjects))
    if(filteredProjects):
        print(f"\n\n📂 Found {len(filteredProjects)} project(s) associated with 📧 {email}:\n\n")
        for index, project in enumerate(filteredProjects):
            print(f"📝 Project {index}:")
            print(json.dumps(project, indent=4))  
            print("-" * 40)  

    else:
        print(f"⚠️ No projects found for 📧 {email}.")

# =====================================================================
#                       delete Projects
# ========================================================================

def delete_UserProjects(email):
    allProjects=read_allData("./Crowd-Funding-console-app/users_projects.json")
    userProjects = list(filter(lambda project: project["email"] == email, allProjects))

    if not userProjects:
        print(f"⚠️ No projects found for 📧 {email}. Nothing to delete.")
        return

    filteredProjects = list(filter(lambda project: project["email"] != email, allProjects))
    update_file(filteredProjects,"./Crowd-Funding-console-app/users_projects.json")
    print(f"✅ All {len(userProjects)} project(s) associated with 📧 {email} have been successfully deleted! 🗑️")


# =====================================================================
#                       remove project by title
# ========================================================================


def remove_project_by_title(email):
    allProjects=read_allData("./Crowd-Funding-console-app/users_projects.json")
    userProjects = list(filter(lambda project: project["email"] == email, allProjects))

    if not userProjects:
        print(f"⚠️ No projects found for 📧 {email}. Nothing to delete.")
        return
    projectTitle = input("📝 Please enter the title of the project you want to delete: ").strip()
    remaining_projects = [project for project in allProjects if not (project["email"] == email and project["title"] == projectTitle)]

    update_file(remaining_projects, "./Crowd-Funding-console-app/users_projects.json")
    print(f"✅ Project '{projectTitle}' has been successfully deleted! 🚀")
    

# =====================================================================
#                       Edit project 
# ========================================================================

Update_actions = {
    "1": "title",
    "2": "description",
    "3": "totalTarget",
    "4": "startDate",
    "5": "endDate",
    "6": "✅ Done! No more updates needed."
}
def update_menu():
    print("\n🔄 **Update Project Details** 🔄")
    print("=================================")
    print("🔹 1️⃣  Update Project **Title** 📝")
    print("🔹 2️⃣  Update Project **Description** 🖊️")
    print("🔹 3️⃣  Update Project **Total Target** 💰")
    print("🔹 4️⃣  Update Project **Start Date** 📅")
    print("🔹 5️⃣  Update Project **End Date** ⏳")
    print("🔹 6️⃣  ✅ Done! No more updates needed. 🔙")
    print("=================================")
    choice = input("📌 Enter your choice (🔢 1 to 6): ").strip()
    return choice

def check_updatedDate(keyToUpdate,projectToUpdate):
    while True:
        validated_date = get_valid_date(f"\n📅 Enter the new value for ${keyToUpdate} (YYYY-MM-DD):")

        if not validated_date:
            print("❌ Invalid date format! Please enter a valid date in **YYYY-MM-DD** format.")
            continue

        if keyToUpdate == "endDate":
            start_date = get_valid_date("You have to enter start date\n\n")  
            if validated_date < start_date:
                print(f"⚠️ The **end date** must be after the start date ({projectToUpdate['startDate']}). Try again.")
                continue

        elif keyToUpdate == "startDate":
            end_date = get_valid_date("You have to enter end date\n\n")  
            if validated_date > end_date:
                print(f"⚠️ The **start date** must be before the end date ({projectToUpdate['endDate']}). Try again.")
                continue

        projectToUpdate[keyToUpdate] = validated_date.isoformat()
        break 

    return projectToUpdate

def Edit_userProject(email):
    allProjects=read_allData("./Crowd-Funding-console-app/users_projects.json")
    userProjects = list(filter(lambda project: project["email"] == email, allProjects))

    if not userProjects:
        print(f"⚠️ No projects found for 📧 {email}. Nothing to delete.")
        return
    projectTitle = input("📝 Please enter the title of the project you want to update: ").strip()

    projectToUpdate = next((project for project in userProjects if project["title"] == projectTitle), None)
    
    if not projectToUpdate:
        print(f"⚠️ No project found with the title '{projectTitle}' under your account.")
        return

    

    choice=update_menu()
    while True:
        if choice in Update_actions and choice != "6":  
            keyToUpdate = Update_actions[choice]
            if keyToUpdate in ["startDate", "endDate"]:
                 
                projectToUpdate=check_updatedDate(keyToUpdate,projectToUpdate)

            else:

                newValue = input(f"✏️ Enter the new value for {keyToUpdate}: ").strip()
                
                projectToUpdate[keyToUpdate] = newValue
            clear_console()

            print("✅ Update successful!")  
            print("🔄 If you want to update another field, please choose an option from 1 to 5.")
            print("🔙 Otherwise, select 6 ")
            
            choice=update_menu()


        else:
            break    

       
    remaining_projects = [project for project in allProjects if not (project["email"] == email and project["title"] == projectTitle)]
    remaining_projects.append(projectToUpdate) 
    update_file(remaining_projects, "./Crowd-Funding-console-app/users_projects.json")
    print(f"✅ Project '{projectTitle}' has been successfully updated! 🚀")
    
