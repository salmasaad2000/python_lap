import re
import json
from datetime import datetime

# File paths
USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"

# Utility functions
def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def validate_phone(phone):
    return re.match(r"^01[0-2,5]{1}[0-9]{8}$", phone)


def validate_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)


# Authentication
def register():
    users = load_data(USERS_FILE)

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")

    if not validate_email(email):
        print("Invalid email format!")
        return

    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")
    if password != confirm_password:
        print("Passwords do not match!")
        return

    phone = input("Enter Mobile Phone: ")
    if not validate_phone(phone):
        print("Invalid Egyptian phone number!")
        return

    users.append({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "activated": True  
    })
    save_data(USERS_FILE, users)
    print("Registration successful! You can now log in.")


def login():
    users = load_data(USERS_FILE)
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            if user["activated"]:
                print(f"Welcome, {user['first_name']}!")
                return user
            else:
                print("Account not activated!")
                return None
    print("Invalid email or password!")
    return None


# Project management
def create_project(user):
    projects = load_data(PROJECTS_FILE)

    title = input("Enter Project Title: ")
    details = input("Enter Project Details: ")
    target = input("Enter Total Target Amount (EGP): ")
    try:
        target = float(target)
        if target <= 0:
            raise ValueError("Target must be a positive number.")
    except ValueError:
        print("Invalid target amount!")
        return

    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if start_date >= end_date:
            print("Start date must be before end date!")
            return
    except ValueError:
        print("Invalid date format!")
        return

    projects.append({
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "owner": user["email"]
    })
    save_data(PROJECTS_FILE, projects)
    print("Project created successfully!")


def view_projects():
    projects = load_data(PROJECTS_FILE)
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        print(project)


def edit_project(user):
    projects = load_data(PROJECTS_FILE)
    title = input("Enter the title of the project you want to edit: ")

    for project in projects:
        if project["title"] == title and project["owner"] == user["email"]:
            print("Editing project:", project)
            project["title"] = input("New Title: ") or project["title"]
            project["details"] = input("New Details: ") or project["details"]
            project["target"] = float(input("New Target: ") or project["target"])
            save_data(PROJECTS_FILE, projects)
            print("Project updated successfully!")
            return
    print("Project not found or unauthorized!")


def delete_project(user):
    projects = load_data(PROJECTS_FILE)
    title = input("Enter the title of the project to delete: ").strip()
    
    matched_projects = [p for p in projects if p["title"] == title and p["owner"] == user["email"]]
    
    if matched_projects:
        projects = [p for p in projects if not (p["title"] == title and p["owner"] == user["email"])]
        save_data(PROJECTS_FILE, projects)
        print("Project deleted successfully!")
    else:
        print("No project found with that title under your ownership. Please try again.")


def search_project_by_date():
    projects = load_data(PROJECTS_FILE)
    date_str = input("Enter date (YYYY-MM-DD) to search: ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        results = [p for p in projects if datetime.strptime(p["start_date"], "%Y-%m-%d") <= date <= datetime.strptime(p["end_date"], "%Y-%m-%d")]
        if results:
            for result in results:
                print(result)
        else:
            print("No projects found for this date.")
    except ValueError:
        print("Invalid date format!")


# Main menu
def main():
    while True:
        print("\nCrowdfunding Console App")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\nProject Management")
                    print("1. Create Project")
                    print("2. View All Projects")
                    print("3. Edit Your Project")
                    print("4. Delete Your Project")
                    print("5. Search Projects by Date")
                    print("6. Logout")
                    sub_choice = input("Choose an option: ")
                    if sub_choice == "1":
                        create_project(user)
                    elif sub_choice == "2":
                        view_projects()
                    elif sub_choice == "3":
                        edit_project(user)
                    elif sub_choice == "4":
                        delete_project(user)
                    elif sub_choice == "5":
                        search_project_by_date()
                    elif sub_choice == "6":
                        break
                    else:
                        print("Invalid option! Try again.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
