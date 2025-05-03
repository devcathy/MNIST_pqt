import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
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
        menu_view = menu.addMenu('View') # 그룹생성
        # 메뉴 객체 생성
        file_exit = QAction('Exit', self)
        file_exit.setShortcut('command + Q') # 단축키 설정하기 
        file_exit.setStatusTip("누르면 영원히 빠이빠이")
        new_txt = QAction("텍스트 파일", self)
        new_py = QAction('파이썬 파일', self)
        view_stat = QAction("상태표시줄", self, checkable = True) # 체크박스가 활성화 되어있기 때문에 이 메뉴의 체크 박스 활성화 되어있을 것이ㅏㄷ. 
        # view_stat 과 menu_view 를 연결을 시켜야함
        view_stat.setChecked(True)
        
        
        
        
        
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        view_stat.triggered.connect(self.tglStat)
        # 서브그룹 추가 
        file_new = QMenu('New', self)
        # 서브 메뉴 추가
        file_new.addAction(new_txt)
        file_new.addAction(new_py)
        menu_view.addAction(view_stat)# view 라는 그룹에 view_stat 이라는 메뉴 추가됨
        # 상태표시줄이라는 메뉴가 나왔고 체크가 되어있는 상태이다. 
        # check 누르면 , check 사라지고 , 다시 check 된다. 
        menu_File.addMenu(file_new)
        menu_File.addAction(file_exit) # 주메뉴 추가
        
        self.resize(450, 500)
        self.show()
        
    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
            
    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)
        
        quit = cm.addAction("Quit")
        # 오른 클릭 했을 떄 Quit 이 나온다. 
        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        # 마우스 오른 클릭해서 quit 누르면 창 꺼짐
        
        if action==quit:
            qApp.quit()
            
        
        
        
app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())



