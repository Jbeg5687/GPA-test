# Joshua Begley
# GPA test
# Asks the user to enter their name and GPA and checks if they qualify for the 
# Dean's List and Honor Roll.

def check_student_qualification():
    while True:
        # Ask for the student's last name
        last_name = input("Enter the student's last name (type 'ZZZ' to quit): ")

        # If the user enters 'ZZZ', the program will stop
        if last_name.upper() == 'ZZZ':
            print("Thank you! Exiting the program.")
            break  # Exit the loop and end the program

        # Ask for the student's first name
        first_name = input("Enter the student's first name: ")

        # Ask for the student's GPA and make sure it's a number
        try:
            gpa = float(input(f"Enter {first_name} {last_name}'s GPA (e.g., 3.8): "))
        except ValueError:
            print("Oops! That doesn't look like a number. Please enter a valid GPA.")
            continue  # Restart the loop to get correct input

        # Check if the GPA qualifies for the Dean's List and Honor Roll
        if gpa >= 3.5:
            print(f"Congratulations! {first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"Congratulations! {first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List this time.")
            print(f"{first_name} {last_name} did not qualify for the Honor Roll this time.")

if __name__ == "__main__":
    check_student_qualification()