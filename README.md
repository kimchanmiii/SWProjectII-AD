# SWProjectII-AD
PyQt5를 이용한 타이핑게임 제작 

## 1. 개요    
### 1.1 프로젝트 개요    
최근에 추억의 게임이라면서 타자 게임을 하는 친구들의 모습을 볼 수 있었다. 또한, 과 특성상 라이브 코딩같은 시험을 보는 경우에 타자의 속도는 시험의 결과에도 영향을 미칠 수 있다. 이러 한 점을 고려해 수업시간에 자주 사용되는 단어나 코딩을 할 때 쓰이는 단어들을 연습하고자 타 자 게임을 만들었다. 우리가 쉽게 접할 수 있는 타자 게임과 수업시간에 배운 내용을 접목하여 우리만의 타자 게임을 만들었다. 우리가 만든 타자 게임은 그냥 타자만 연습하는 그런 프로그램 들과는 달리 여러 이미지와 효과를 주어 진짜 게임처럼 만들었다. 이러한 점에서 사용자는 재미 를 느낄 수 있다. 이번 프로젝트의 조건이 PyQt5가 필수로 적용해야되는 만큼 우리는 최대한 PyQt5를 이용해보고자 다른 프로그램은 사용하지 않고 PyQt5만 이용하여 게임을 만들었다. PyQt5에 포함되어 있는 많은 클래스들을 적극 활용하여 여러 이미지와 효과가 있는 타자 게임을 개발하였다.

## 2. 개발내용및결과물    
### 2.1 목표    
우리가 소프트웨어 소속의 학생들인 만큼 그냥 일반적인 타자 게임과는 달리 게임에서 다루는 단 어들을 소프트웨어에서만 볼 수 있는 단어들만 추가해 코딩을 할 때의 속도와 수업시간에 다루는 언어들에 대해 조금 더 친숙해질 수 있는 그런 타자 게임을 개발하고자 한다. 이 타자 게임을 통 해 수업시간에 배운 내용을 상기시킬 수 있을 뿐만 아니라 PyQt5를 적극 활용해 타자 게임 시작 버튼을 눌렀을 때 나오는 이미지를 통해 게임의 진행상태를 나타내어 사용자에게 시각적으로 즐 거움을 더해주는 그런 게임을 만들고자 한다.    
### 2.2 연구/개발 내용 및 결과물    
#### 2.2.1 연구/개발 내용    
먼저 게임에 대한 간략한 소개를 하자면, 정글을 탈출해야하는 미션이 걸린 타자 게임이라고 보 면 된다. 플레이어가 타자 게임을 시작하는 버튼을 누름과 동시에 새로운 창이 뜨면서 게임 화면 이 나타난다. 타자 게임 창에서는 단어들이 위에서 떨어지고, 게임 화면 창에서는 게임 속 캐릭터 들이 움직인다. 위에서 떨어지는 단어를 입력하면 캐릭터가 악어로부터 한 칸 멀어지고, 단어가 창의 끝에 도달할 때 까지 입력하지 못하면 악어가 캐릭터에게 한 칸 전진하도록 제작하였다. 게 임 속 캐릭터가 집에 도달할 때 까지 악어에게 잡히지 않으면 미션 성공, 잡히게 되면 미션 실패 하는 게임이다.
이 게임에 총 2가지 언어, 3가지 단계 중 하나를 선택할 수 있게끔 제작하였다. 2가지 언어는 한 국어와 영어가 있는데 한국어를 선택하면 타자 게임에 한국어가 나오면서 한글 타자를 연습할 수 있고, 영어를 선택하면 영어 단어들이 나오면서 영어 타자를 연습할 수 있다. 3가지 단계는 초급, 중급, 그리고 전문가 총 세가지 이다. 이 세개의 단계는 단어가 떨어지는 속도로 차이를 두었다. 초급은 단어가 천천히 그리고 전문가로 갈수록 단어가 빨리 내려오도록 만들었다.    
#### 2.2.2 활용/개발된 기술의 알고리즘 <코드분석>
| 파일.클래스 | 기능 |
| --- | --- |
| window.CWidget | 타자 GUI 윈도우 생성 |
| map.CMap | 타이핑 GUI 기능 구현 |
| map.CWord | 특정 단어에 특정 좌표 설정 |
| main.Main | 사용자의 게임 진행 상태를 나타내는 이미지창 |
| user.User | 게임 중인 사용자의 이미지 |
| win.Win | 게임 성공했을 때의 사용자 이미지 |
| croco.Croco | 사용자에게 압박감과 몰입감을 주는 악어 이미지 |
| ground.Ground | 배경 이미지 |
| house.House | 사용자의 최종 목적지인 집 이미지 |
| endbutton.Fail | 게임 실패했을 때의 이미지창 |
| endbutton.Success | 게임 성공했을 때의 이미지 창 |                          

#### 주요클래스
1. QGraphicsView: 주로 QGraphicsScene과 함께 쓰이며 이미지를 실제로 시각화 해준다.
2. QGraphicsScene: 다수의 2D 그래픽 항목을 관리하기 위해 사용한다. 실제로 시각화를하는 기능을 가지고 있지 않아서 주로 QGraphicsView와 함께 쓰인다.
3. QGraphicsPixmapItem: QGraphicsScene에 추가할 수 있는 픽스맵 항목을 제공한다. 이미지를 객체로 생성 가능하다.
4. Thread: 동시에 같은 작업들을 처리하여 전체적인 성능을 향상시키거나 루틴의 흐름을 중단 시키지 않고 별개의 작업 흐름이 서브 루틴을 실행하여 서로 다른 작업을 함께 진행할 때에 사용한다.
5. Lock: 한 번에 하나의 thread만 사용할 수 있는 자원의 액세스 구간에 Lock을 설치하면 Lock을 획득한 thread 하나만 실행되고 나머지는 기다리게 한다.
6. QPointF: 정밀한 부동 소수 점을 이용하여 점의 위치를 지정한다.
7. QPainter: 위젯이나 다른 그림 그리기 기능 위에 그림 그리는데에 편리하다. 일반적인 도형은 물론이고 글씨를 나타내는 것도 가능하다.

#### 2.2.3 현실적 제한 요소 및 그 해결 방안   
처음에 게임을 시작할 때 메인에서 타자게임창을 뜨게 하였더니 마지막에 모든 프로그램을 종료 해도 그 타자 게임창은 사라지지 않고 직접 닫기 버튼을 눌러야만 한 점이 아쉽다. 그 점을 보안 하기 위해서는 처음 클래스를 설계할 때부터 메인 파일 실행 시 바로 타자 게임 창을 띄우도록 하는 게 아니라, 클래스 안에서 객체를 생성함으로써 나중에는 다른 클래스 파일에서도 그 타자 게임 창을 닫을 수 있도록 해야한다. 실제로 구현 가능 하지만 처음의 설계를 뒤엎는 일이기에 시간이 오래 걸리는데 프로젝트의 제출 기한에 맞추기에는 어려움이 있어 수정하지 못한 점이 아 쉽다.
