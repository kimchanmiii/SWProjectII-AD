import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import map


class CWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 컨트롤 레이아웃 박스
        self.vbox = QVBoxLayout()   #QVBoxLayout()=>수직 레이아웃 객체를 생성한다
        self.hbox = QHBoxLayout()   #QHBoxLayout()=>수평 레이아웃 객체를 생성한다

        # 한글 영어 선택
        self.lang = QComboBox()   #QComboBox()=>여러 개의 선택지 중 하나만 선택할 때에 편리한 객체를 생성한다
        self.lang.addItem('한글')  #addItem('')=>QComboBox에 선택지를 추가한다
        self.lang.addItem('영어')
        self.lang.setCurrentIndex(0) #인덱스를 이용하여 생성한 QComboBox의 기본 선택지을 설정한다

        # 난이도
        self.level = QComboBox()  #한글, 영어를 선택하는 방식과 같은 방식으로 난이도를 선택하는 QComboBox를 생성한다
        self.level.addItem('초보자')
        self.level.addItem('중급자')
        self.level.addItem('전문가')
        self.level.setCurrentIndex(0)

        # 단어 입력창
        self.edit = QLineEdit()   #QLineEdit()=>입력 가능한 한 줄 길이의 문자열 상자 객체를 생성한다

        # 게임 시작버튼
        self.btn = QPushButton('게임시작')     #QPushButton()=>버튼 객체를 생성한다
        self.btn.setCheckable(True)           #setCHeckable=>메소드 인자가 True인 경우 누른 상태와 눌려있지 않은 상태를 구분한다
        self.btn.clicked.connect(self.toggleButton)    #connect 메소드를 이용하여 self.btn이 눌렸을 때 self.toggleButton 함수로 연결한다


        # 수평 레이아웃 위젯 추가
        self.hbox.addWidget(self.lang)   #=>.addWidget메소드를 사용하여 수평 레이아웃에 위젯을 추가한다
        self.hbox.addWidget(self.level)
        self.hbox.addWidget(self.edit)
        self.hbox.addWidget(self.btn)

        self.vbox.addStretch(1)          #수직 레이아웃에 여백 공간을 추가한다
        self.vbox.addLayout(self.hbox)   #수직 레이아웃에 수평 박스를 추가한다
        self.setLayout(self.vbox)        #수직 레이아웃을 메인 레이아웃으로 설정한다
        self.setGeometry(100, 100, 500, 500)    #.setGeometry=>윈도우의 시작 위치와 크기를 설정한다
                                                # 윈도우는 (100, 100) 위치에서 시작하고 크기는 가로 500, 세로 500로 설정한다
        self.setWindowTitle('정글을 탈출하라!')   #.setWindowTitle=>윈도우의 타이틀을 설정한다/윈도우의 타이틀은 '정글을 탈출하라!'

        self.map = map.CMap(self)    #map모듈에 있는 CMap클래스의 객체 생성한다
        #self.word = Word(self)


    def closeEvent(self, e):  #윈도우를 닫는 이벤트가 발생할때, self.map에 있는 gameOver()함수를 실행한다
        self.map.gameOver()

    def paintEvent(self, e):
        qp = QPainter();   #QPainter()=>위젯이나 다른 그림 그리기 장치에 그림그리기 위해 쓰이는 객체를 생성한다
        qp.begin(self)     #QpaintDevice 여기서 self는 QWidget
                            # .begin()=>boolean형태를 리턴하며 성공적으로 그림그리기 장치를 불러왔는지 확인한다
        self.map.draw(qp)  #self.map에 있는 draw()함수 실행한다
        qp.end()           # .end()=>QPainter() 사용을 종료한다

    def toggleButton(self, state):

        if state:
        # .currentIndex())=>QComboBox의 현재 인덱스를 가져온다. 사용자가 선택한 언어와 난이도에 따라 self.map에있는 gameStart함수를 실행한다
            self.map.gameStart(self.lang.currentIndex(), self.level.currentIndex())
            self.btn.setText('게임종료')    # .setTExt(')btn의 텍스트를 설정한다
            self.lang.setEnabled(False)    # .setEnabled(boolean)=>QComboBox 무력화할지 결정한다.
                                            # 메소드의 인자 값이 음수일 경우 QComboBox를 무력화한다
            self.level.setEnabled(False)


        else:
            self.map.gameOver()         #self.map에 있느  gameOver함수를 실행한다
            self.btn.setText('게임시작')   # .setTExt(')btn의 텍스트를 설정한다
            self.lang.setEnabled(True)  # .setEnabled(boolean)=>QComboBox 무력화할지 결정한다.
                                        # 메소드의 인자 값이 음수일 경우 QComboBox를 무력화한다
            self.level.setEnabled(True)


    def keyPressEvent(self, e):  #키보드 입력 받는 함수

        self.edit.setFocus()     # .setFous()=>self.edit에 초점을 설정한다

        if e.key() == Qt.Key_Return:            #엔터키 입력되었을 때  입력된 단어를 확인한다
            self.map.delword(self.edit.text())  #맞다면, self.map에 있는 delword함수를 실행한다
            self.edit.setText('')               #self.edit의 텍스트를 빈 문자열('')로 지정한다



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()        #CWidget()의 객체를 생성한다
    w.show()             #CWidget()시각화한다
    sys.exit(app.exec_())




