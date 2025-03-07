import bcrypt
import json
import os

def save_Data_inJsonFile(newData,fileName):
    data=read_allData(fileName)
    if not newData:  
        print("❌ No data to save!")
        return
    
    data.append(newData)
    with open(fileName, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ New data added successfully!")


def read_allData(fileName):
    if not os.path.exists(fileName) or os.stat(fileName).st_size == 0:
        return []
    try:
        with open(fileName, "r") as file:
            loaded_data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
            print("⚠️ Warning: The JSON file is empty or corrupted. Returning an empty list.")
            return []  

    return loaded_data    



def update_file(newfile,filename):
    if not newfile:  
        print("❌ No data to save!")
        return
    with open(filename, "w") as file:
        json.dump(newfile, file, indent=4)



def isUserExist(email):
    allUsers=read_allData("./Crowd-Funding-console-app/user_data.json")
    filteredUser = list(filter(lambda user: user["email"] == email, allUsers))
    if(filteredUser):
        return True,filteredUser
    else:
        return False,[]

def hash_password(password):
    salt = bcrypt.gensalt()  
    hashed_password = bcrypt.hashpw(password.encode(), salt)  
    return hashed_password


def check_hashedPassword(entered_password, stored_hashed_password):
#    json save hashed password as string but bcrypt.checkpw compare bytes so i encode both passwords
#  encode convert string to bytes
    return bcrypt.checkpw(entered_password.encode(), stored_hashed_password.encode())

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows ('cls') or Linux/macOS ('clear')


def isUserHasProjects(email):
    allProjects=read_allData("./Crowd-Funding-console-app/users_projects.json")
    filteredProjectsForUser = list(filter(lambda user: user["email"] == email, allProjects))
    if(filteredProjectsForUser):
        return True,filteredProjectsForUser
    else:
        return False,[]

def is_project_title_unique_for_user(email,title):
    exists,userProjects=isUserHasProjects(email)
    if exists:
        filteredProjectsForUser = list(filter(lambda project: project["title"] == title, userProjects))
        if  filteredProjectsForUser:
            print("\n\n❌ Oops! A project with this name already exists. 🚨\n🔄 Please choose a different project name.\n\n")
            return False
    return True
    

        