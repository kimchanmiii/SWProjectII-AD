from PyQt5.QtCore import QPointF, QRect
from PyQt5.QtGui import QFont
from threading import Thread, Lock
from random import randint
from time import sleep
from endButton import Success, Fail
from main import Main

# 언어에 따라 튜플 단어장을 생성한다
kor = ('국민대학교', '인터페이스', '객체 배열', '레퍼런스', '가비지', '딕셔너리', '집합', '소프트웨어프로젝트2', '단위테스트', '알고리즘', '프로그래밍')
eng = ('QHBoxLayout', 'class', 'roslaunch', "Canny", 'super()', 'implements', 'getter', 'setter', 'void', 'byte', 'numpy.ndarray', 'hsv',
       'self', 'int', 'Inteager', 'QPushButton', 'eval', 'connect', 'if', 'addWidget', 'append', 'insert', 'add', 'abstract', 'extends', 'hangman', 'list')


class CWord:

    def __init__(self, pt, word):
        # 단어 좌표
        self.pt = pt
        # 단어 문자
        self.word = word


class CMap:

    def __init__(self, parent):
        self.parent = parent
        self.rect = parent.rect()              #현재의 가로 크기
        self.word = []                         #나중에 랜덤으로 뽑힌 단어를 담을 리스트를 생성한다
        self.thread = Thread(target=self.play) #CMap에 있는 play 메소드를 대상으로 동시에 같은 작업들을 처리할 수 있도록 하는 Thread()객체를 생성한다
        self.bthread = False                   #처음에는 thread를 비활성화한다
        self.lock = Lock()                     #객체를 잠금하고 해제하는 기능을 제공하는 Lock()객체를 생성한다
        self.main = Main()                     #게임의 현재 게임 진행 상태를 시각화한 Main()객체를 생성한다
        self.success = Success()               #성공했을 경우의 객체를 생성한다
        self.fail = Fail()                     #실패했을 경우의 객체를 생성한다


    def __del__(self):
        self.gameOver()                 #소멸자 메소드로서 gameOver함수를 실행한다

    def gameStart(self, lang, level):   #QComboBox에서 얻어온 인덱스를 그대로 사용한다
        self.lang = lang
        self.level = level
        self.main.view.show()           #게임 시작 버튼을 누르면 우리의 현재 게임 진행 상태를 나타내는 윈도우창 시각화한다


        self.bthread = True                        #게임이 시작되면 thread를 활성화하여 play함수가 동시에 실행되도록 한다
        if self.thread.is_alive() == False:        #thread가 동작 중인지 확인하고 thread가 동작하지 않는다면,
            self.thread = Thread(target=self.play) #play 메소드를 대상으로 동시에 같은 작업들을 처리할 수 있도록 하는 Thread()객체를 생성한다
            self.thread.start()                    #위 코드에서 생성한 객체를 시작한다


    def gameOver(self):
        self.bthread = False    #게임이 끝나면 thread 비활성화한다
        self.word.clear()       #랜덤으로 뽑힌 단어들이 담긴 리스트를 초기화한다
        self.parent.update()    #부모 클래스의 update()함수 실행한다
        self.main.view.close()  #게임이 끝날 때 우리의 현재 게임 진행 상태를 나타내는 윈도우창을 닫는다




    def draw(self, qp):                     #qp=>QPainter()
        qp.setFont(QFont('맑은 고딕', 12))   # .setFont()=> 글씨체, 글씨 크기 설정한다
        self.lock.acquire()                 # .acquire=>만약 self.lock이 잠겨있지 않았다면 자신의 상태를 변경하면서 즉시 리턴한다
        for w in self.word:                 #랜덤으로 뽑힌 단어들이 담긴 리스트에서 반복문 사용하여,
            qp.drawText(w.pt, w.word)       # .drawText메소드를 이용하여 타자 게임 창에 단어를 나타나게 한다
        self.lock.release()                 # .release=>리소스에 대한 사용을 마친다


    def createWord(self):        #hangman 게임에서 secretWord를 지정한 것과 마찬가지로, randint메소드를 사용하여 임의의 수를 뽑고
                                # 이 숫자를 문자열의 인덱스를 가리키는 데에 사용하여 self.word에 있는 단어를 무작위로 뽑아낸다

        self.rect = QRect(self.parent.rect())

        str = ''
        if self.lang == 0:              #게임이 한국어 버전으로 실행되는 경우
            n = randint(0, len(kor)-1)
            str = kor[n]
        else:                           #게임이 영어 버전으로 실행되는 경우
            n = randint(0, len(eng)-1)
            str = eng[n]

        x = randint(0, self.rect.width() - 50)  #문자가 시작되는 위치도 무작위로 설정 하기 위하여 x좌표를 지정할 때 randint메소드를 사용한다
        y = 0

        cword = CWord(QPointF(x, y), str)     #QPointF(x,y)=>좌표 값으로 변환한다. CWord클래스를 사용하여 특정 문자열에 특정 좌표 값을 대응한다
        self.word.append(cword)               #좌표 값을 가진 문자열을 self.word라는 리스트에 추가한다


    def downWord(self, speed):      #단어가 일정 속도를 유지하며 아래로 떨어질 수 있도록 한다

        i = 0

        for w in self.word[:]:                  #단어가 바닥에 닿을 때까지 입력하지 않았을 경우, 단어의 y좌표 값을 더하여 아래로 떨어지도록 한다
            if w.pt.y() < self.rect.bottom():
                w.pt.setY(w.pt.y() + speed)
                i += 1

            else:
                del (self.word[i])              #결국 사용자가 입력하지 못하고 단어가 바닥에 닿았을 경우, 단어를 삭제한다
                self.main.noTyping = True       #사용자가 주어진 단어 입력 실패를 나타내고 악어의 이동 여부를 나타내는 변수로서
                                                # True일 경우, 악어가 전진한다

    def delword(self, str):

        self.lock.acquire()

        i = 0
        find = False                #단어를 바르게 입력했는지 확인하기 위한 변수이다
        for w in self.word[:]:
            if str == w.word:       #입력한 단어가 주어진 단어와 같은 경우, 단어들이 모여 있는 리스트에서 해당 단어를 삭제한다
                del (self.word[i])
                find = True         #True로 설정하여 단어가 바르게 인식되었다고 인식한다
                break
            else:
                i += 1
        self.lock.release()

        if find:                        #단어를 바르게 입력했을 경우,
            self.parent.update()        #부모 클래스의 update()메소드를 실행한다
            self.main.isCorrect = True  #사용자가 주어진 단어 입력 성공을 나타내고 사용자의 이동 여부를 나타내는 변수로서 True일 경우, 사용자가 전진한다



    def play(self):

        while self.bthread:             #thread가 활성화 되었을 때

            if randint(1, 200) == 1:
                self.lock.acquire()
                self.createWord()       #무작위로 뽑은 단어 리스트 완성하기
                self.lock.release()

            self.lock.acquire()
            if self.level == 0:         #'초급자'일 경우 speed는 0.5이다. downWord함수를 실행하여 지정한 속도에 맞춰 단어가 아래로 떨어지도록 한다
                self.downWord(0.5)
            elif self.level == 1:       #'중급자'일 경우 speed는 0.7이다. downWord함수를 실행하여 지정한 속도에 맞춰 단어가 아래로 떨어지도록 한다
                self.downWord(0.7)
            else:                       #'전문가'일 경우 speed는 0.9이다. downWord함수를 실행하여 지정한 속도에 맞춰 단어가 아래로 떨어지도록 한다
                self.downWord(0.9)
            self.lock.release()

            self.parent.update()
            sleep(0.01)

            if self.main.user.x <= self.main.croco.x+250:     #사용자와 악어가 맞닿았을 때(게임 실패했을 때)
                self.fail.show()                              #실패 이미지를 시각화한다
                if self.fail.mouseIs == True:                 #버튼이 눌렸을 때 gameOver함수를 실행한다
                    self.gameOver()
                    self.fail.close()                         #실패 이미지창을 닫는다

            elif self.main.user.x > 690:                      #사용자가 목표 지점까지 도달한 경우(게임 성공했을 때)
                self.success.show()                           #성공 이미지를 시각화한다
                self.main.user.setVisible(False)              #게임 진행 중인 사용자의 이미지는 보이지 않도록 지정한다
                self.main.win.setVisible(True)                #게임 성공한 사용자의 이미지는 보이도록 지정한다
                if self.success.mouseIs == True:              #버튼이 눌렸렸을 때 gameOver함수를 실행한다
                    self.gameOver()
                    self.success.close()                      #성공 이미지창을 닫는다








