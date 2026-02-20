import openpyxl 
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side   
def create_excel_file(file_name):
    # Create a new workbook and select the active sheet
    workbook = Workbook()
    sheet = workbook.active

    # Set the title of the sheet
    sheet.title = "Data"

    # Define the header row
    headers = ["ID", "Name", "Age", "City"]
    sheet.append(headers)

    # Add some sample data
    data = [
        [1, "tom", 30, "New York"],
        [2, "Bob", 25, "Los Angeles"],
        [3, "Charlie", 35, "Chicago"],
        [4, "David", 28, "Houston"]
    ]

    for row in data:
        sheet.append(row)

    # Save the workbook to a file
    workbook.save(file_name)
    
if __name__ == "__main__":    create_excel_file("sample_data.xlsx")