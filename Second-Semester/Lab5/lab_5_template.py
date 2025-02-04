"""
Name:
Section: 02
Description: Template for Lab 5
"""

"""
Scenario: we live in a world where blackbaud no longer exists. our job is to write
a student records program that can print out the transcript, grade level, and email of our students.
You are to implement this using functions, dictionaries, and lists
"""


def getStudent(directory, student, gradelevel):
    """
        Function Name: getStudent
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type: Multiple returns of all values associated to the keys at directory[student] 
        Description:
            A Function that returns all of the values associated to the keys in the dictionary at key "student"
    """

    # Prompt for student name and store the input

    name = input("Enter student's name: ")
    grade = int(input("Enter student's grade level: "))
    email = input("Enter student's email: ")
    directory[name] = {"name": name, "grade": grade, "email": email, "grades": {}}
    print(f"Student {name} added successfully.")
    name = student

    gradelevel = grade
        
    pass

def getStudentGrades(directory, student):
    """
        Function Name: getStudentGrades
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type: Dictionary of Student Gradebook
        Description:
            A Function that returns a Dictinary of the student's gradebook at dictionary[student]
    """
    print("the students grades:", directory[student][""]) # TODO FIX CAUSE DOES NOT EXIST
    

    pass

def getStudentGradeLevel(directory,student):
    """
        Function Name: getStudentGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  integer corresponding to student's grade level
        Description:
            A Function that returns a Dictionary of the student's gradebook at dictionary[student]
    """
    print("the students grades:", directory[student]["grade"])

    pass

def getStudentEmail(directory,student):
    """
        Function Name: getStudentGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  string corresponding to student's email
        Description:
            A Function that returns a string of the student's email at dictionary[student]
    """
    print("the students grades:", directory[student]["email"])
    pass

def getStudentsByGradeLevel(directory, gradelevel, student):
    """
        Function Name: getStudentsbyGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            gradelevel <int> : integer corresponding to the grade level
            Return Type:  none
        Description:
            procedure that prints out all of the students of a corresponding grade level.
    """

    print("the students by grade", directory[gradelevel])

    pass

def addStudent(directory):
    """
        Function Name: addStudent
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            Return Type:  none
        Description:
            procedure that adds a student with the following values: <dict> grades, <int> grade level, <string> email to the <dict>directory
    """
    name = input("Students name: ")
    grade = int(input("Enter the students grade level: "))
    email = input("Enter the email: ")
    directory[name] = {"name": name, "grade": grade, "email": email, "grades": {}}

    pass

def removeStudent(directory, student):
    """
        Function Name: removeStudent
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  none
        Description:
            procedure that removes the student at directory[student]
    """
    if student in directory:
        del directory[student]
        print(f"{student} removed")

    pass

def updateGrade(directory, student):
    """
     Function Name: updateGrades
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  none
        Description:
            procedure that updates a student's gradebook
    """
    if student in directory:
        subject = input("Enter the student just like how it is in the hasmap: ")
        grade = int(input("Enter the grade for teh subject: "))
        directory[student]["grades"][subject] = grade




    pass


def calculateGPA(directory, student, gpa):
    """
     Function Name: calculateGPA
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <float> average of all grades
        Description:
            creates a GPA variable set equal to zero, then computes the average (mean) of all of the grades in the gradebook
    """
    # https://stackoverflow.com/questions/7002429/how-to-extract-all-values-from-a-dictionary-in-python REMEMBTER 
    
    if student in directory:
        grades = directory[student]["grades"].values()
        gpa = sum(grades) / len(grades)
        print(f"GPA is: {gpa}")
    return gpa

    
    pass


def checkHonorRoll(directory,student, gpa):
    """
     Function Name: checkHonorRoll
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <bool> True or False depending on a student has made the honor roll or not
        Description:
            Calls the calculateGPA() subroutine that gets the GPA then checks all grades in the grade book to see if they are all over 81, then returns True or False depending on if the GPA is 88 or better
    """
    if student in directory:
        if gpa <= 88:
            print("This student is on honor roll")
        else:
            print("This student is not on honor roll")
    
    


    pass

def printMenu():
    """ 
         Function Name: printMenu
        Parameters:
           none
        Description:
            prints out the menu with 7 menu options, along with an 8th one corresponding to quitting out of the function
    """
    print("\n Chc Student Directory:")
    print("1. Add Student")
    print("2. RM Student")
    print("3. Get Student")
    print("4. Update Grades")
    print("5. Calcualte GPA")
    print("6. Get Student Grade Level")
    print("7. Exit")


pass

def main(student, directory):
    #TODO: Implement every function in main
    #Students = {"Student Name": 0, "Student Email": 0, "Student Grade Level": 0, "Student GPA": 0, } 
    #student = {
    #    "student1": {"name": "", "grade": 0, "email": "", "grades": 0},
    #}

    while True:
        printMenu()
        user_choice = input("Enter a choice between 1-7: ")

        if user_choice == "1":
            addStudent(directory)
        elif user_choice == "2":
            student_name = input("Enter the student to remove: ")
            removeStudent(student)
        elif user_choice == "3":
            student_name = input("Enter the student to retrieve: ")
            getStudent(student)
        elif user_choice == "4":
            student_name = input("Enter the student to update grades: ")
            updateGrade(student)
        elif user_choice == "5":
            student_name = input("Enter the student for GPA calculation: ")
            print(f"GPA: {calculateGPA(student)}")
        elif user_choice == "6":
            student_name = input("Enter the student for grade level: ")
            getStudentGradeLevel(student)
        elif user_choice == "7":
            exit()
            
            
            break


    pass

if __name__ == "__main__":
    main()

