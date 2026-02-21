import sys, PyQt6 
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QPlainTextEdit, QLabel
)
from PyQt6.QtCore import Qt
from datetime import datetime

class MainWindow(QMainWindow):
    n2 = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("입력 → 출력 기록 예제")
        self.resize(600, 400)

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # 출력창 (로그가 쌓이는 곳)
        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        from PyQt6.QtGui import QFont
        self.output.setFont(QFont("Consolas", 10))
        main_layout.addWidget(self.output, stretch=1)  # 출력창이 공간 대부분 차지

        # 입력 영역 (하단)
        input_layout = QHBoxLayout()
        
        label = QLabel("입력:")
        label.setFixedWidth(60)
        input_layout.addWidget(label)

        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText("여기에 입력 후 엔터...")
        input_layout.addWidget(self.input_edit)

        btn_send = QPushButton("보내기")
        btn_send.setFixedWidth(100)
        input_layout.addWidget(btn_send)

        main_layout.addLayout(input_layout)

        # 연결: 엔터키 또는 버튼 클릭으로 처리
        self.input_edit.returnPressed.connect(self.process_input)
        btn_send.clicked.connect(self.process_input)

        # 초기 메시지 (선택)
        self.append_log("시스템: 입력을 기다리고 있습니다...")

    def process_input(self):
        #공백 없애고 입력값 가져오기
        self.text = self.input_edit.text().strip()
        # 입력값이 "숫자/문자열" 형태인지 확인
        if len(self.text) < 2:
            response = "입력 형식이 올바르지 않습니다. '숫자/문자열' 형태로 2자 이상 입력해주세요."
            self.append_log(f"velmora: {response}")
            return 0
        else:
            if self.text.count('/') != 1:
                response = "입력 형식이 올바르지 않습니다. '숫자/문자열' 형태로 입력해주세요."
                self.append_log(f"velmora: {response}")
                return 0
            else:
                txt = self.text.split('/')
                try:
                    self.n = int(txt[0])
                    self.t = txt[1]
                    if self.t == None or self.t == "":
                        self.t = "미입력"
                except ValueError   :
                    response = "숫자를 입력해주세요."
                    self.append_log(f"velmora: {response}")
                    return 0
                
                if self.text == None or self.text == "":
                    response = "빈 입력은 처리할 수 없습니다."
                    self.append_log(f"velmora: {response}")
                    return 0
                elif len(self.t) > 25:
                    response = "문자열은 25자 이하로 입력해주세요."
                    self.append_log(f"velmora: {response}")
                    return 0
                #n이 양수이고 t가 문자열이며 길이가 25자 이하이고 빈 문자열이 아니며 숫자가 포함되어 있지 않은 경우
                elif self.n > 0 and isinstance(self.t, str) and not any(c.isdigit() for c in self.t) and len(self.t) <= 25 and self.t != "":
                    self.n2 += self.n
                    # 입력한 내용 출력창에 기록
                    
                    response= "처리완료."
                    self.append_log(f"velmora: {self.n} {self.t} {self.n2} {self.text} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {response}")

                    # 응답도 출력창에 기록
                    self.append_log(f"velmora: {response}")

                    # 입력창 지우기 (선택사항)
                    self.input_edit.clear()
                    # 또는 유지하고 싶으면 주석 처리

                    # 자동 스크롤
                    self.output.ensureCursorVisible()
                    return 0
                else:
                    response = "숫자/문자로 이루어진 올바른 입력이 아닙니다. 숫자는 양수여야 하고, 문자열은 25자 이하이며 숫자를 포함하지 않아야 합니다."
                    self.append_log(f"velmora: n: {self.n} t:{self.t} n2: {self.n2} text: {self.text} {response}")
                    return 0


    def append_log(self, message: str):
        self.output.appendPlainText(message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()