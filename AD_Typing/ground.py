from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem


SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 492
GROUND_HEIGHT = 100
FRAME_PER_MS  = 16

class Ground(QGraphicsPixmapItem):     #QGraphicsPixmapItem클래스는 QGraphicsScene에 추가 할 수 있는 픽스맵(비트의 지도) 항목을 제공한다

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap('typing_img/background.png'))  #setPixmap()=>픽스맵 지정, QPixmap=>이미지 처리 클래스
        self.x = 0            #객체의 x좌표를 지정한다

    def game_update(self):                  #timer event가 발생할 때 실행될 함수
        self.x -= 1                         #객체의 x좌표 -= 1
        self.setPos(self.x, GROUND_HEIGHT)  #변화된 x좌표 반영하여 이미지의 위치를 다시 지정한다
        if self.x < -1000:                  #Ground()는 배경을 나타내는 클래스로서, 변화된 이미지를 효율성있게 사용 가능하도록 이미지 좌표를 다시 지정한다
            self.x += 2000

