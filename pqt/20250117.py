# 파이썬과 운영체제가 소통할때 필요하다.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# QWidget 상속받아서 class 만든다. 
# 나만의 창을 만드는 class 를 만든다. 
class Exam(QWidget):
    def __init__(self):
        # 상위객체 Qwidget 에 해당하는 객체를 만들어 줘야한다 
        super().__init__() # super() 이렇게 하면 상위객체 생성, 생성된 상위객체 .__init__() 해주기 (생성자 호출해주기)
        self.initUI()
    
    # 메서드 생성
    def initUI(self):
        # 인자: 버튼안에 들어갈 문구, self = 나 자신에게 버튼을 추가하겠다.
        btn = QPushButton('abcd', self)
        # 특정 객체가 들어가면 그 객체에 맞추어 크기를 조정한다. 
        # btn.sizeHint(): 글씨를 기준으로 사이즈를 조정해준다. 
        btn.resize(btn.sizeHint())
        # 마우스를 버튼에 가져다 대면 이 버튼은 무엇을 하는 버튼인지에 대한 설명을 쓸수 있다. 
        # / 굵게 표시를 종료한다. 
        btn.setToolTip('툴팁입니다.<b>안녕하세요<b/>')    
        # 창의 맨 왼쪽 위 기준으로 왼쪽으로 부터 거리, 위에서 부터의 거리
        btn.move(20, 30)
        
        
        
        # 창크기 조정
        # 내 화면에서의 위치 300, 300(좌표다), 가로 400, 세로 500
        self.setGeometry(300, 300, 400, 500)
        # 창의 이름
        self.setWindowTitle('첫 번째 학습')
        self.show()
        # 어찌되었든 보이긴 해야하니까 
        
        
        
    
# main 함수 만들기
# 모든 qt5 어플리케이션은 어플리케이션 오브젝트를 생성해야함
# 즉 어플리케이션 객체를 생성해야함
# sys.argv ci에서 명령줄로 인수를 받아들일때 꼭 써야함

app = QApplication(sys.argv)

# 내가 만든 창을 만드는 객체 
# 위의 클래스 객체를 생성 
w = Exam()

# 나갈때 무조건 있어야 한다. 
# 프로그램 깨끗하게 종료
# 결과가 return 되는 부분
# app.exec_() 이벤트 루프를 시작하는 부분 (사용자가 버튼을 클릭하거나 키포드를 누르는 행위를 할때 까지 기다리는 것, 즉 기다림의 상태)
# 루프가 끝날때 exit 가 시작
sys.exit(app.exec_())
