import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QPlainTextEdit, QLabel
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
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
        text = self.input_edit.text().strip()
        if not text:
            return  # 빈 입력 무시

        # 1. 입력한 내용 출력창에 기록
        self.append_log(f"> {text}")

        # 2. 여기서 원하는 처리 (예시)
        if text.lower() in ["안녕", "hello"]:
            response = "안녕하세요! 반갑습니다 😄"
        elif text.lower() == "시간":
            from datetime import datetime
            response = f"현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            response = f"받은 메시지: {text} (처리됨)"

        # 3. 응답도 출력창에 기록
        self.append_log(f"  ↳ {response}")

        # 4. 입력창 지우기 (선택사항)
        self.input_edit.clear()
        # 또는 유지하고 싶으면 주석 처리

        # 자동 스크롤
        self.output.ensureCursorVisible()

    def append_log(self, message: str):
        self.output.appendPlainText(message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()