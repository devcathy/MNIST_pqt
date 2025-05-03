import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication
class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 상태표시줄임
        self.statusBar()
        # 상태표시줄에 값을 받아옴
        self.statusBar().showMessage("안녕하세요")
        # 메뉴바는 생성한 뒤에 뭘 계속 추가해야함 
        # 따라서 객체를 생성해야함
        # 메뉴생성 실패함 - mac os 에서는 menu.setNativeMenuBar(False) 이 코드가 추가 되어야함
        menu = self.menuBar() # 메뉴바생성
        menu.setNativeMenuBar(False)
        menu_File = menu.addMenu('File')
        menu_Edit = menu.addMenu('Edit')
        # 메뉴 객체 생성
        file_exit = QAction('Exit', self)
        file_exit.setShortcut('command + Q') # 단축키 설정하기 
        file_exit.setStatusTip("누르면 영원히 빠이빠이")
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction('파이썬 파일', self)
        
        
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        # 서브그룹 추가 
        file_new = QMenu('New', self)
        # 서브 메뉴 추가
        file_new.addAction(new_txt)
        file_new.addAction(new_py)
        
        menu_File.addMenu(file_new)
        menu_File.addAction(file_exit) # 주메뉴 추가
        
        self.resize(450, 500)
        self.show()
        
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())



