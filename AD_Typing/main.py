from PyQt5.QtCore import (
     Qt,
    QBasicTimer
)
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView
)
from ground import Ground
from house import House
from user import User
from crocodile import Croco
from win import Win


#Main=>타자 게임을 실행하고 현재 상태를 알려주는 게임 윈도우GUI
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 490
GROUND_HEIGHT = 0
FRAME_PER_MS  = 16

                            #QGraphicsScene이랑 QGraphicsView는 같이 쓰인다
class Main(QGraphicsScene): #QGraphicsScene는 다수의 2D그래픽 항목을 관리하기 위한 표면을 사용된다. 자체로 시각화하지 않는다

    def __init__(self, parent=None, FRA=None):
        super().__init__(parent)

        self.isCorrect = None   #사용자가 주어진 단어 입력 성공을 확인하는 변수이다
        self.noTyping = None    #사용자가 주어진 단어 입력 성공을 확인하는 변수이다
        self.isClear = None     #게임 종료 후 버튼이 눌렸는지 확인하기 위한 변수이다



        self.timer = QBasicTimer()           # QBasicTimer()=>timer events을 제공한다
        self.timer.start(FRAME_PER_MS, self) # .start(int msec)=>주어진 msec주기로 타이머를 시작하거나 재시작한다


        self.back1 = Ground()                #배경 이미지를 가진 Ground객체를 생성한다
        self.back1.setPos(0,GROUND_HEIGHT)   # .setPos(x, y)=>위치를 지정한다
        self.addItem(self.back1)             # .addItem('')=>QGrahphicsScene에 항목을 추가한다


        self.back2 = Ground()                #배경 이미지를 가진 Ground객체를 생성한다
        self.back2.x = 1000                  #생성한 객체의 x좌표를 지정한다
        self.back1.setPos(0,GROUND_HEIGHT)   # .setPos(x, y)=>위치를 지정한다
        self.addItem(self.back2)             # .addItem('')=>QGrahphicsScene에 항목을 추가한다


        self.user = User()                  #게임 진행 중인 사용자 이미지를 가진 User객체를 생성한다
        self.user.setPos(180, 320)          # .setPos(x, y)=>위치를 지정한다
        self.addItem(self.user)             # .addItem('')=>QGrahphicsScene에 항목을 추가한다


        self.croco = Croco()                #악어 이미지를 가진 Croco객체를 생성한다
        self.croco.setPos(-130, 350)        # .setPos(x, y)=>위치를 지정한다
        self.addItem(self.croco)            # .addItem('')=>QGrahphicsScene에 항목을 추가한다


        self.house = House()                #게임 성공의 목적지인 집의 이미지를 가진 House객체를 생성한다
        self.house.setPos(700,250)          # .setPos(x, y)=>위치를 지정한다
        self.addItem(self.house)            # .addItem('')=>QGrahphicsScene에 항목을 추가한다


        self.win = Win()                    #게임 성공했을 때의 사용자 이미지를 가진 Win객체를 생성한다
        self.win.setPos(800,390)            # .setPos(x, y)=>위치를 지정한다
        self.addItem(self.win)              # .addItem('')=>QGrahphicsScene에 항목을 추가한다
        self.win.setVisible(False)          #self.win으로 생성한 객체를 보이지 않도록 지정한다



        self.view = QGraphicsView(self)                               #QGrahicsView()=>구상한 QGraphicsScene을 시각화한다
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #가로 방향 스크롤을 off로 설정한다
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   #세로 방향 스크롤을  off로 설정한다
        self.view.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)           # .setFixedSize()=>self.view의 크기 고정한다
        self.setSceneRect(0,100, SCREEN_WIDTH, SCREEN_HEIGHT)         # .setFixedSize()=>self.view의 시작 위치와 크기 고정한다



    def timerEvent(self, event):  #일정 주기로 timer event를 제공하면서 실시간으로 이미지나 기능들을 업데이트한다
        self.game_update()
        self.update()



    def game_update(self):
        self.back1.game_update()     #self.back1에 있는 game_update()함수 실행=>배경이미지로서, 움직이는 이미지 연출 가능하다
        self.back2.game_update()     #self.back1에 있는 game_update()함수 실행=>배경이미지로서, 움직이는 이미지 연출 가능하다
        if self.isCorrect == True:   #사용자가 주어진 문자 타이핑에 성공한 경우,
            self.user.game_update()  #self.user에 있는 game_update()함수 실행=>한 칸 씩 앞으로 이동한다
            self.isCorrect = False   #다시 False로 지정
        if self.noTyping == True:    #사용자가 주어진 문자 타이핑에 실패한 경우,
            self.croco.game_update() #self.croco에 있는 game_update()함수 실행=>한 칸 씩 앞으로 이동한다
            self.noTyping = False    #다시 False로 지정











