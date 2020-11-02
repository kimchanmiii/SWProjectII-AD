from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 492
FRAME_PER_MS  = 16


class User(QGraphicsPixmapItem): #QGraphicsPixmapItem클래스는 QGraphicsScene에 추가 할 수있는 픽스맵(비트의 지도) 항목을 제공한다

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap('typing_img/user_ing.png'))  #setPixmap()=>픽스맵 지정, QPixmap=>이미지 처리 클래스
        self.x = 180   #객체의 x좌표 지정한다




    def game_update(self):       #timer event가 발생할 때 실행될 함수
        self.x += 30              #한 번에 객체의 x좌표 30씩 이동한다
        self.setPos(self.x, 320)  #변화된 x좌표 반영하여 이미지의 위치를 다시 지정한다


