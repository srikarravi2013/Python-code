import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  


def calc_grade(class_avg: float, final_test: float) -> float:
    return (class_avg * 0.60) + (final_test * 0.40)


def get_letter_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    return 'F'


def extract_student_data(file_path: str) -> list:
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return []
    except ET.ParseError as e:
        print(f"XML Parsing Error: {e}")
        return []

    students = []
    for student in root.findall('student'):
        student_profile = {
            "id": student.attrib.get('id'),
            "name": student.attrib.get('name'),
            "semesters": []
        }

        for semester in student.findall('semester'):
            sem_data = {
                "term": semester.attrib.get('term'),
                "subjects": []
            }

            for subject in semester.findall('subject'):
                class_avg_text = subject.find('class_avg')
                final_test_text = subject.find('final_test')
                
                if class_avg_text is not None and final_test_text is not None:
                    sem_data["subjects"].append({
                        "name": subject.attrib.get('name'),
                        "class_avg": float(class_avg_text.text),
                        "final_test": float(final_test_text.text)
                    })

            student_profile["semesters"].append(sem_data)
        students.append(student_profile)

    return students


def display_report_cards(student_list: list):
    if not student_list:
        print("No student records found or data could not be parsed.")
        return

    print("\nSTUDENT REPORT CARD SYSTEM:")

    for student in student_list:
        s_name = student["name"]
        s_id = student["id"]

        print(f"\nStudent: {s_name} (ID: {s_id})")

        for semester in student["semesters"]:
            term_name = semester["term"]

            print(f"  Term: {term_name}")
            print("    Subject Class Avg Final Test Total Grade")

            for subject in semester["subjects"]:
                sub_name = subject["name"]
                avg = subject["class_avg"]
                test = subject["final_test"]

                final_score = calc_grade(avg, test)
                letter = get_letter_grade(final_score)

                print(f"    {sub_name} {avg}% {test}% {final_score:.2f}% [{letter}]")
            print()


def plot_subject_grades(student_list: list):
    if not student_list:
        print("No data available to plot.")
        return

    subject_data = {}

    for student in student_list:
        student_id = student["id"]
        for semester in student["semesters"]:
            term_name = semester["term"]
            for subject in semester["subjects"]:
                sub_name = subject["name"]
                avg = subject["class_avg"]
                test = subject["final_test"]

                overall_grade = calc_grade(avg, test)

                if sub_name not in subject_data:
                    subject_data[sub_name] = {
                        "ids": [],
                        "grades": [],
                        "terms": []
                    }

                subject_data[sub_name]["ids"].append(str(student_id))
                subject_data[sub_name]["grades"].append(overall_grade)
                subject_data[sub_name]["terms"].append(term_name)

    for subject_name, data in subject_data.items():
        plt.figure(figsize=(8, 5))

        ids = data["ids"]
        grades = data["grades"]
        terms = data["terms"]

        colors = ['darkorange' if '2' in str(t) else 'darkblue' for t in terms]

        plt.scatter(ids, grades, c=colors, edgecolor='black', s=100, alpha=0.8, zorder=3)

        plt.title(f"Overall Grades Distribution: {subject_name}", fontsize=14)
        plt.xlabel("Student ID", fontsize=12)
        plt.ylabel("Overall Grade (%)", fontsize=12)
        plt.ylim(0, 105)
        plt.grid(True, linestyle='--', alpha=0.5, zorder=0)

        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Term 1', markerfacecolor='darkblue', markersize=10, markeredgecolor='black'),
            Line2D([0], [0], marker='o', color='w', label='Term 2', markerfacecolor='darkorange', markersize=10, markeredgecolor='black')
        ]
        plt.legend(handles=legend_elements, loc='lower left')

        plt.tight_layout()
        plt.show()



    xml_file_path = r"C:\Users\srika\Desktop\Python code\Book.xml"
    extracted_data = extract_student_data(xml_file_path)
    display_report_cards(extracted_data)
    plot_subject_grades(extracted_data)