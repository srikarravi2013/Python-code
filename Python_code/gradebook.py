def generate_a_list(student_name):
    marks = []
    subjects = ["Math", "Science", "ELA"]
    
    print(f"Enter marks for {student_name}: " )
    
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter {subject} mark: "))
                marks.append(mark)
                break  
            except ValueError:
                print("invalid input! Please enter the grades.")
                
    return marks


student_system = {}

print("Grade System (Math, Science, ELA):")

while True:
    name = input("\nEnter student name (or type 'exit' to finish): ").strip()
    
    if name.lower() == 'exit':
        break
    
    if name in student_system:
        print('This name is already registered please enter a different name')
        continue

        
    if name == "":
        print("Name cannot be empty.")
        continue

    student_system[name] = generate_a_list(name)

print("\n---Final Student Grades---")

print(f'\nThe Best overall in the class is {max(student_system)}')

for name, marks in student_system.items():

    average = sum(marks) / len(marks)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
        
    print(f"Student: {name} | Average: {average:.2f} | Grade: {grade}")
