import os
import random
from string import ascii_uppercase as uppercase
from string import digits
import time

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Attendance Management System")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Add Student")
    print("4. Update Student data")
    print("5. Save Attendance in CSV")
    print("6. Go to welcome page")
    print("0. Exit")

def check_username_exists(username):
    try:
        with open("Projects list\\Attendance Management system\\login_info.csv", "r") as f:
            for line in f.readlines():
                if line.strip():
                    fields = line.split(",")
                    if fields[2].strip() == username:  # Check the username field
                        return True
        return False
    except FileNotFoundError:
        return False

def signup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sign up with your details, system will assign you a unique ID.")
    print("-" * 100)
    
    name = input("Enter your full name: ")
    gender = input("Select Gender (M/F): ")
    while True:
        username = input("Enter your username: ")
        if check_username_exists(username):
            print("Username already exists. Please try a different username.")
        else:
            break

    password = input("Create Password: ")
    
    # 10 character unique ID, first five characters are capital letters and last five characters are digits
    unique_id = "".join(random.sample(uppercase, k=5) + random.sample(digits, k=5))
    print(f"Your unique ID is {unique_id}")
    print("Save it in a safe place. You will need it to login.")
    print("You have successfully signed up!")
    print("Bringing you back to the main menu.")
    time.sleep(4)
    main_menu()
    print("-" * 100)
    
    # Adding column names to the file if it is empty
    if not os.path.exists("Projects list\\Attendance Management system\\login_info.csv") or os.stat("Projects list\\Attendance Management system\\login_info.csv").st_size == 0:
        with open("Projects list\\Attendance Management system\\login_info.csv", "w") as f:
            f.write("name,gender,username,password,unique_id\n")
    
    with open("Projects list\\Attendance Management system\\login_info.csv", "a") as f:
        f.write(f"{name},{gender.upper()},{username},{password},{unique_id}\n")

# calling the function to check
signup()
