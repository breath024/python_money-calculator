import sys

from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag
from PyQt6.QtWidgets import QDialogButtonBox, QLabel, QPushButton, QVBoxLayout, QWidget, QApplication, QDialog, QMainWindow, QInputDialog, QLineEdit, QHBoxLayout, QFormLayout, QPlainTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App name")
        self.resize(450, 180)           # 창 크기 좀 작게 → 필요하면 나중에 키우기

        # 중앙 위젯 + 수평 레이아웃으로 버튼과 입력창 나란히 배치
        central = QWidget()
        self.setCentralWidget(central)
        
        # 입력창 3줄 전부다 복붙하면 추가됨
        self.input_lable = QLineEdit()
        self.input_lable.setPlaceholderText("입력...")
        self.input_lable.setFixedHeight(36)  # 입력창 

        # 이건 출력창
        self.output_lable = QPlainTextEdit()
        self.output_lable.setReadOnly(True)
        self.output_lable.setPlaceholderText("출력...")
        self.output_lable.setFixedHeight(100)  # 출력창 
        

        # 작은 버튼 만들기
        button = QPushButton("Press me!")
        button.setFixedWidth(140)         # 버튼 폭 고정 → 작고 예쁘게
        # button.setFixedSize(140, 40)    # 원하면 높이도 고정 가능
        button.clicked.connect(self.show_custom_dialog)
        
        layout = QVBoxLayout(central)
        layout.addWidget(button)
        layout.addSpacing(20)  # 버튼과 아래 그룹 사이 간격

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setSpacing(10)

        form_layout.addRow(self.output_lable)
        form_layout.addRow(self.input_lable)

        layout.addLayout(form_layout)
        layout.addStretch()

    def show_custom_dialog(self):
        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
            self.output_lable.setText("대화상자 OK 눌렀음!")
        else:
            print("Cancel!")
            self.output_lable.setText("취소했어요~")


    def button_click(self, s):
        print("click", s)

        dlg1 = QDialog(self)
        dlg1.setWindowTitle("HELLO!")
        dlg1.exec()

    def button_clicked(self, s):
        print("click", s)
        dlg2 = CustomDialog()
        if dlg2.exec():
            print("Success!")
        else:
            print("Cancel!")
            
    def showdialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok and text:
            print("Your name is:", text)
        if ok:
            self.label.setText(text)

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept) # 버튼이 클릭되면 accept() 메서드가 호출되어 대화 상자가 닫히고, exec() 메서드는 True를 반환합니다.
        self.buttonBox.rejected.connect(self.reject) # 버튼이 클릭되면 reject() 메서드가 호출되어 대화 상자가 닫히고, exec() 메서드는 False를 반환합니다.

        layout = QVBoxLayout()                              # 가상 레이아웃 생성
        message = QLabel("Something happened, is that OK?") # 레이블 함수를 불러오는 동시에 메세지 설정 및 message 변수에 저장
        layout.addWidget(message)                           # 가상 레이아웃에 윗줄 글 추가
        layout.addWidget(self.buttonBox)                    # 가상 레이아웃에 버튼 추가
        self.setLayout(layout)                              # 가상 레이아웃을 실제 레이아웃으로 설정
    

def main():
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()