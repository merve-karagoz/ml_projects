from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
 
def show_win():
   victory_win = QMessageBox()
   victory_win.setText('Doğru!\nHoverboard kazandınız')
   victory_win.exec_()


def show_lose():
   victory_win = QMessageBox()
   victory_win.setText('Hayır, 2015\'te\nMarkalı bir poster kazandınız')
   victory_win.exec_()
 
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Crazy People\'dan yarışma')
main_win.resize(400, 200)
 
question = QLabel('Kanal hangi yılda YouTube\'dan "altın düğme" aldı?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
 
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
 
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)
 
btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
 
main_win.show()
app.exec_()
