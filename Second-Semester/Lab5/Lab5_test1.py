name = input("Enter students name: ")
grade = int(input("Enter students grade level: "))
email = input("Enter students email: ")
    
student_identificatin_for_dict = f"student{len(directory) + 1}"
directory[student_identificatin_for_dict] = {"name": name, "grade": grade, "email": email}
print(f"Student {name} added.")