print("Welcome to the student information system !")

student_info = {
    "Name" : input("Enter your name: "),
    "DOB" : input("Enter your date of birth (DD/MM/YYYY): "),
    "Course" : input("Enter your course: "),
    "Inter percentage" : input("Enter your intermediate percentage: "),
    "Subjects" : input("Enter your subjects: "),
}

ask1 = str(input("Want to see your info?: ")).lower()

if ask1 == "yes":
    print(student_info)
else:
    print("Thankyou!")

def cal_average(percentage):
    total = sum(percentage)
    count = len(percentage)
    average = total / count
    return average

ask2 = input("Do you want to calculate average of your subjects?: ").lower()

if ask2 == "yes":
    percentage = []
    num_subjects = int(input("Enter the number of subjects: "))
    for i in range(num_subjects):
        subject_percentage = input(f"Enter marks of subject {i+1}: ")
        percentage.append(subject_percentage)
    average_percentage = cal_average(percentage)
    print(f"The average percentage is: {average_percentage:.2f}")
else:
    print("Thankyou!")