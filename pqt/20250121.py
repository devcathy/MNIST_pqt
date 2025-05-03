import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton("Push me!!", self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # 클릭 하면 시그널 발생, 따라서 application 나가는 효과 생김
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        self.resize(500, 500)
        self.setWindowTitle("두 번째 시간")
        self.show()
    
    
    # 버튼을 눌러서 종료 시키는 것이 아니라 
    # x 를 눌러서 종료 시켰을 때 출려됨    
    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?",
                             QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        
        
        
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())