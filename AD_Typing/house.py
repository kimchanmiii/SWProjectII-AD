from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 492
FRAME_PER_MS  = 16

class House(QGraphicsPixmapItem):       #QGraphicsPixmapItem클래스는 QGraphicsScene에 추가 할 수있는 픽스맵(비트의 지도) 항목을 제공한다

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap('typing_img/house.png')) #setPixmap()=>픽스맵 지정, QPixmap=>이미지 처리 클래스
        self.x = 800    #객체의 x좌표를 지정한다








