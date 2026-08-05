import xml.etree.ElementTree as ET
from openpyxl import load_workbook as lw


def extract_finance_data(file_path):
    file_path_lower = file_path.lower()
    
    if file_path_lower.endswith('.xml'):
        return _extract_from_xml(file_path)
    elif file_path_lower.endswith('.xlsx'):
        return _extract_from_xlsx(file_path)
    else:
        print("Error: Unsupported file format. Please provide a .xml or .xlsx file.")
        return []


def _extract_from_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return []
    except ET.ParseError as e:
        print(f"XML Parsing Error: {e}")
        return []

    # Final record that are returned
    finance_records = []
    
    # Check for all months in the file
    for month_node in root.findall('month'):
        month_profile = {
            "month_name": month_node.attrib.get('name'),
            "expenses": []
        }
        # Check for tvhe expenses in that selected month aboe
        for expense in month_node.findall('expense'):
            category = expense.attrib.get('category')
            # pulls out the expense cost
            amount_text = expense.text
            
            # Safety check to make sure it is not empty
            if category is not None and amount_text is not None:

                month_profile["expenses"].append({
                    "category": category,
                    "amount": float(amount_text)
                })

        finance_records.append(month_profile)

    return finance_records


def _extract_from_xlsx(file_path):
    try:
        # Load workbook (reads values, not formulas)
        wb = lw(file_path, data_only=True)
        sheet = wb.active 
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return []

    # Convert sheet rows into a list
    rows = list(sheet.iter_rows(values_only=True))
    if not rows:
        return []

    # Get the category names from row 1 (skipping 'Month' in Column A)
    header_row = rows[0]
    categories = [str(cat).strip() for cat in header_row[1:] if cat is not None]

    finance_records = []

    # Process each monthly data  row (starting at row 2)
    for row in rows[1:]:
        # Skip empty rows
        if not row or row[0] is None:
            continue
            
        month_name = str(row[0]).strip()
        expenses = []
        
        # Match each category column with its cell value
        for idx, category in enumerate(categories):
            col_idx = idx + 1 # Categories start at Column B (index 1)
            if col_idx < len(row):
                amount_val = row[col_idx]
                if amount_val is not None:
                    try:
                        amount = float(amount_val)
                        expenses.append({
                            "category": category,
                            "amount": amount
                        })
                    except ValueError:
                        continue
                        
        finance_records.append({
            "month_name": month_name,
            "expenses": expenses
        })

    return finance_records


def generate_monthly_report(name: str, salary: float, target_month: str, finance_records: list):
    
    # Flag to check if python actually finds the month in the data list
    month_found = False
    
    # Loop through the list of month profiles
    for month_profile in finance_records:
        # Match the month name 
        if month_profile["month_name"].lower() == target_month.lower():
            month_found = True
            
            print("\n")
            print(f"PERSONAL FINANCE REPORT FOR {name.upper()}")
            print("--------------------")
            print(f"Month: {month_profile['month_name']}")
            print('--------------------')
            
            total_expenses = 0.0
            
            # Loop through the nested list of expense dictionaries
            for expense in month_profile["expenses"]:
                category = expense["category"]
                amount = expense["amount"]
                
                print(f"{category}: ${amount:.2f}")
                total_expenses += amount
                
            # Savings Calculation
            savings = salary - total_expenses
            
            print("--------------------")
            print(f"Total Expenses: ${total_expenses:.2f}")
            print(f"Savings:        ${savings:.2f}")
            print("--------------------")
            break  # Exit the loop once the correct month is processed
            
    if not month_found:
        print(f"\nCould not generate report: No data found for '{target_month}'.")


def get_user_inputs():
    name = input("Enter your name: ")
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            break
        except ValueError:
            print("Please enter a valid number for salary.")
    target_month = input("Enter the target month: ")
    return name, salary, target_month


# 1. Get inputs from user
u_name, u_salary, target_month = get_user_inputs()

# 2. Extract data from the Excel file using a relative path
file_path = 'Book.xlsx'
records = extract_finance_data(file_path)

# 3. Generate the report if records was loaded correctly
if records:
    generate_monthly_report(u_name, u_salary, target_month, records)