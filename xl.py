import openpyxl 
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, Border, Side
from datetime import datetime, timedelta



dlt = datetime(datetime.now().year, 1, 1)
print(dlt) 
try:
    load_workbook("입출금내_" + datetime.now().strftime('%Y')+'.xlsx')
    print("파일이 이미 존재합니다.")
except FileNotFoundError:
    wb = Workbook()
    ws = wb.active
    
    for i in range(0, 12):
        wb.create_sheet(f"{i+1}월")
        headers = ["날짜", "입금액", "출금액", "출금처","목적분류", "잔액"]
        ws = wb[f"{i+1}월"]
        ws.append(headers)
        ws.column_dimensions['A'].width = 15
        ws.column_dimensions['B'].width = 12
        ws.column_dimensions['C'].width = 12
        ws.column_dimensions['D'].width = 25  # 출금처는 길게
        ws.column_dimensions['E'].width = 15
        for col in range(1, 6):
            ws.cell(1, col).font = Font(bold=True)
        ws['A2'] = dlt.strftime('%Y-%m-%d')
        dlt += timedelta(days=1)
        i = 2
        while dlt.strftime('%d') != '01':
            i += 1
            ws[f"A{i}"] = dlt.strftime('%Y-%m-%d')
            dlt += timedelta(days=1)
    wb.save("입출금내역_" + datetime.now().strftime('%Y')+'.xlsx')




def create_format():

    dlt = datetime.now() + timedelta(days=1)
    try:
        load_workbook("입출금내역_" + datetime.now().strftime('%Y')+'.xlsx')
        print("파일이 이미 존재합니다.")
        return 0
    except FileNotFoundError:
        wb = Workbook()
        ws = wb.active

        dlt += timedelta(days=1)
        headers = ["날짜", "입금액", "출금액", "출금처", "잔액"]
        ws.append(headers)
        ws.column_dimensions['A'].width = 15
        ws.column_dimensions['B'].width = 12
        ws.column_dimensions['C'].width = 12
        ws.column_dimensions['D'].width = 25  # 출금처는 길게
        ws.column_dimensions['E'].width = 15
        for col in range(1, 6):
            ws.cell(1, col).font = Font(bold=True)
        ws['A2'] = datetime.now().strftime('%Y-%m-%d')
        i = 2
        while dlt.strftime('%d') != '01':
            i += 1
            ws[f"A{i}"] = dlt.strftime('%Y-%m-%d')
            dlt += timedelta(days=1)
        wb.save("입출금내역_" + datetime.now().strftime('%Y')+'.xlsx')