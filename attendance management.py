import os, csv
import random
from string import ascii_uppercase as uppercase
from string import digits
import time



# Function for the user/faculty to sign up
def signup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sign up with your details, system will assign you a unique ID.")
    print("-" * 100)
    
    name = input("Enter your full name: ")
    gender = input("Select Gender (M/F): ")
    while True:
        username = input("Enter your username: ")
        if check_if_exists("Projects list\\Attendance Management system\\login_info.csv", username, 2):
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


# Function for the faculty to login
def login():
    print("Login with your username and password.")
    print("-" * 100)
    username = input("Enter your username/id: ")
    password = input("Enter your password: ")
    
    try:
        with open("Projects list\\Attendance Management system\\login_info.csv", "r") as f:
            for line in f.readlines():
                if line.strip():
                    fields = line.split(",")
                    if (fields[2].strip() == username or fields[4].strip() == username) and fields[3].strip() == password:
                        print("Login successful!")
                        print(f"Welcome {fields[0]}")
                        print("Bringing you back to the main menu.")
                        time.sleep(4)
                        main_menu()
                        print("-" * 100)
                        return
            print("Invalid username or password. Please try again.")
            
    except FileNotFoundError:
        print("No users have signed up yet. Please sign up first.")
        print("Bringing you back to the main menu.")
        time.sleep(4)
        main_menu()
        print("-" * 100)


# Function to check if the value at the given column index exists in the file
def check_if_exists(file_path, value, column_index):
    try:
        with open(file_path) as f:
            for line in f.readlines():
                if line.strip():
                    fields = line.split(",")
                    if fields[column_index].strip() == value:  # Check the username field
                        return True
        return False
    except FileNotFoundError:
        return False

        
# Function to add student details
def add_student():
    
    number_of_students = int(input("Enter the number of students you want to add: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for i in range(number_of_students):
        print(f"Student {i+1}")
        print("Enter student's details below: ")
        name = input("Name: ")
        roll_no = input("Roll number: ")
        
        if check_if_exists("Projects list\Attendance Management system\student_info.csv", roll_no, 1):
            print("Student already exists in the system. Please enter a different roll number.")
            roll_no = input("Roll number: ")
        
        st_id = input("Student ID: ")
        if check_if_exists("Projects list\Attendance Management system\student_info.csv", st_id, 2):
            print("Student already exists in the system. Please enter a different Id.")
            roll_no = input("Roll number: ")
        phone = input("Phone number: ")
        email = input("Email: ")
        
        if not os.path.exists("Projects list\Attendance Management system\student_info.csv") or os.stat("Projects list\Attendance Management system\student_info.csv").st_size == 0:
            with open("Projects list\Attendance Management system\student_info.csv", "w") as f:
                f.write("Name,Roll Number,Student Id,Phone Number,Email Id\n")
        with open("Projects list\Attendance Management system\student_info.csv", "a") as f:
            f.write(f"{name},{roll_no},{st_id},{phone},{email}\n")
            
    print("Student details added successfully!")
    

# Function to read student information from the file
def read_student_info(file_path):
    students = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    return students


def mark_attendance():
    student_file = "Projects list\\Attendance Management system\\student_info.csv"
    attendance_file = "Projects list\\Attendance Management system\\attendance.csv"
    
    # Ensure the directory exists
    directory = os.path.dirname(attendance_file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Read student information
    students = read_student_info(student_file)
    
    if not students:
        print("No student information found.")
        return

    # Ask for the date
    date = input("Enter the date (YYYY-MM-DD): ")

    # Check if attendance file exists and read its content
    file_exists = os.path.exists(attendance_file)
    if file_exists:
        with open(attendance_file, "r") as f:
            reader = csv.DictReader(f)
            # print(reader)
            attendance_data = list(reader)
            # print(attendance_data)
            existing_headers = reader.fieldnames
            # print(existing_headers)
    else:
        attendance_data = []
        existing_headers = ["Name", "ID"]

    # Add the new date column if it doesn't exist
    if date not in existing_headers:
        existing_headers.append(date)

    # Collect attendance and update the data
    for student in students:
        student_name = student["Name"]
        student_id = student["Student Id"]
        attendance = input(f"Is {student_name} (ID: {student_id}) present? (y/n): ").strip().lower()
        attendance = 'Present' if attendance == 'y' else 'Absent'

        # Find the student's record in the attendance data
        student_found = False
        for record in attendance_data:
            if record["ID"] == student_id:
                record[date] = attendance
                student_found = True
                break

        # If the student is not found, add a new record
        if not student_found:
            new_record = {"Name": student_name, "ID": student_id, date: attendance}
            attendance_data.append(new_record)

    # Write the updated attendance data to the file
    with open(attendance_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=existing_headers)
        writer.writeheader()
        writer.writerows(attendance_data)            

def view_attendance():
    attendance_file = "Projects list\\Attendance Management system\\attendance.csv"
    if not os.path.exists(attendance_file) or os.stat(attendance_file).st_size == 0:
        print("No attendance data found.")
        return

    with open(attendance_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

# First page of the program
def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Attendance Management System")
    print("1. Sign up")
    print("2. Login")
    print("0. Exit")
    
    choice = input("Enter the number of option: ")
    match choice:
        case "1":
            signup()
        case "2":
            login()
        case "0":
            print("Exiting program ......")
            time.sleep(2)
            exit()
        case _:
            print("Invalid input.....")
            print("Exiting the program.")
            time.sleep(2)
            exit()
            

# Main menu of the program    
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Attendance Management System")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Add Student")
    print("4. Save Attendance in CSV")
    print("5. Go to welcome page")
    print("0. Exit")
    
    choice = input("Enter the number of option: ")
    
    match choice:
        case "1":
            mark_attendance()
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            
        case "2":
            view_attendance()
            choice = input("Press any key to go back to the main menu: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            
        case "3":
            add_student()
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            
        case "4":
            print("Saving attendance data to CSV file......")
            time.sleep(2)
            print("Attendance data saved successfully!")
            print("Here is the file path: Projects list\\Attendance Management system\\attendance.csv")
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            
        case "5":
            welcome()
            
        case "0":
            print("Exiting program ......")
            time.sleep(2)
            exit()
            
        case _:
            print("Invalid input.....")
            print("Exiting the program.")
            time.sleep(2)
            exit()
    
if __name__ == "__main__":
    welcome()

