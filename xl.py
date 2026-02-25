import openpyxl 
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, Border, Side
from datetime import datetime, timedelta

# 엑셀 파일 경로
path = "C:\\Users\\USER\\Desktop\\지출내역서\\입출금내역(봇용).xlsx"
# 엑셀 파일 열기

wl = load_workbook(path)
wb = Workbook 
dt = int(datetime.now().strftime('%m')) +1
dlt = datetime.now() + timedelta(days=1)
print("END")
    # 다음날이 1일인 경우 A2 셀부터 다음달 1일까지 날짜 입력
dlt += timedelta(days=4)
i = 2
print(dlt)
while dlt.strftime('%d') != '01':
    i += 1
    dlt += timedelta(days=1)
    print(dlt)

def create_format(file_name):
    # 엑셀 파일 열기
    wl = load_workbook(file_name)
    ws = wl.active 
    # 다음날 날짜 계산
    dlt = datetime.now() + timedelta(days=1)
    # 다음날이 1일인 경우 A2 셀부터 다음달 1일까지 날짜 입력
    if dlt.strftime('%d') == '01':
        dlt += 1
        ws['A2'] = datetime.now().strftime('%Y-%m-%d')
        i = 2
        while dlt.strftime('%d') != '01':
            i += 1
            ws[f"A{i}"] = dlt.strftime('%Y-%m-%d')
            dlt += timedelta(days=1)


    # A1 셀에 현재 날짜와 시간 입력
    ws['A1'] = dt
    # 엑셀 파일 저장
    wl.save(file_name)