from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from qtconsole.qt import QtGui
from window import CWidget

class Fail(QWidget):    #사용자가 실패했을 때

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Fail!")            #setWindowTitle('')=>윈도우의 타이틀 지정한다
        self.setGeometry(300, 300, 400, 300)    #setGeometry(시작 위치, 윈도우 크기)=>윈도우 크기와 위치 지정한다
        self.mouseIs = None                     #버튼이 눌렸는지 확인하는 변수 생성한다


        failImg = QLabel(self)                              #문자열, 이미지 나타내는 데에 편리한 라벨 객체를 생성한다
        failImg.setPixmap(QPixmap("typing_img/fail.png"))   # .setPixmap()=>QLabel에 이미지를 지정한다
        failImg.move(self.width()-330, self.height()-300)   # .move()=>QLabel 위치를 지정한다
        failImg.resize(250, 250)                            # .resize()=>QLabel 크기를 지정한다

        fail = QLabel("Fail! Try again?", self)            #문자열을 담은 라벨 객체를 생성한다
        fail.setFont(QtGui.QFont('맑은 고딕', 15))          # .setFont()=>글씨체와 크기 지정한다
        fail.move(130, 200)
        fail.resize(400,50)

        yesButton = QPushButton("Yes", self)        #문자열을 담은 버튼 객체를 생성한다=>QLabel과 다르게 버튼을 누르는 이벤트 발생 가능하다
        yesButton.move(80, 250)
        yesButton.clicked.connect(self.yesbutton_clicked)   #yesButton이 눌렸을 때 yesbutton_clicked 함수를 실행한다


        noButton = QPushButton("No", self)
        noButton.move(220, 250)
        noButton.clicked.connect(self.noButton_clicked)     #noButton이 눌렸을 때 nobutton_clicked 함수를 실행한다

    def yesbutton_clicked(self):
        self.mouseIs = True     #버튼이 눌렸음을 확인한다
        w2 = CWidget()          #새로운 게임 실행하기 위해 새로운 객체 생성한다
        w2.show()               #위의 코드에서 생성한 객체를 시각화한다

    def noButton_clicked(self):
        self.mouseIs = True     #버튼이 눌렸음을 확인한다


class Success(QWidget):         #사용자가 성공했을 때=>게임의 성공 여부를 나타내는 이미지를 제외하고 실패했을 때와 동일한 방식으로 이루어진다

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Success!")
        self.setGeometry(300, 300, 400, 300)
        self.mouseIs = None


        successImg = QLabel(self)
        successImg.setPixmap(QPixmap("typing_img/success.png"))
        successImg.move(self.width()-330, self.height()-300)
        successImg.resize(250, 250)

        success = QLabel("Success! One more time?", self)
        success.setFont(QtGui.QFont('맑은 고딕', 15))
        success.move(80, 200)
        success.resize(400,50)


        yesButton = QPushButton("Yes", self)
        yesButton.move(80, 250)
        yesButton.clicked.connect(self.yesbutton_clicked)

        noButton = QPushButton("No", self)
        noButton.move(220, 250)
        noButton.clicked.connect(self.noButton_clicked)

    def yesbutton_clicked(self):
        self.mouseIs = True
        w2 = CWidget()
        w2.show()

    def noButton_clicked(self):
        self.mouseIs = True
