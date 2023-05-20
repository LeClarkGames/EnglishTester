from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import *
from app_layout import *
from main_layout import *
from data import *
from random import shuffle, choice

#shuffle(quest_list)
#quest_num = 0
w = choice(quest_list)
w.show_data(result_answ, btn_list)

def click():
    global w
    if answer_btn.text() == "Answer":
        if btn_group.checkedButton():
            w.check_result(btn_list, result)
            sresult()
    else:
        head_lb.show()
        play_lb.show()
        #shuffle(quest_list)
        q = choice(quest_list)
        w.show_data(result_answ, btn_list)
        squestion()

def main():
    main_window.show()
    test_window.hide()

def start():
    main_window.hide()
    test_window.show()

def play_sound():
    global w
    w.make_sound()

exit_btn.clicked.connect(QCoreApplication.instance().quit)
play_lb.clicked.connect(play_sound)
answer_btn.clicked.connect(click)
start_btn.clicked.connect(start)
menu_btn.clicked.connect(main)

answer_btn.setFont(QFont('Arial', 11))
group_box2.setFont(QFont('Arial', 14))
start_btn.setFont(QFont('Arial', 14))
group_box.setFont(QFont('Arial', 13))
exit_btn.setFont(QFont('Arial', 14))
menu_btn.setFont(QFont('Arial', 11))
head_lb.setFont(QFont('Arial', 14))
play_lb.setFont(QFont('Arial', 11))
result.setFont(QFont('Arial', 14))

answer_btn.setFixedSize(285, 28)
menu_btn.setFixedSize(285, 28)
play_lb.setFixedSize(130, 28)

answer_btn.setStyleSheet("background: rgb(0, 0, 0, 100); border-radius: 10px;")
group_box2.setStyleSheet("background: rgb(0, 0, 0, 100); border-radius: 10px;")
group_box.setStyleSheet("background: rgb(0, 0, 0, 100); border-radius: 10px;")
start_btn.setStyleSheet("background: rgb(0, 0, 0, 100); border-radius: 10px;")
exit_btn.setStyleSheet("background: rgb(0, 0, 0, 100); border-radius: 10px;")
menu_btn.setStyleSheet("background: rgb(0, 0, 0, 100); border-radius: 10px;")
play_lb.setStyleSheet("background: rgb(0, 0, 0, 100); border-radius: 10px;")
head_lb.setStyleSheet("background: rgb();")

main_window = QWidget()
main_window.setStyleSheet("background-image: url(E:/Python/English Tester [My Project]/Additional Files/Image/background1.jpg);")
main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
main_window.setWindowTitle("English-Tester")
main_window.setLayout(main_line)
main_window.resize(1366, 768)
main_window.show()

test_window = QWidget()
test_window.setStyleSheet("background-image: url(E:/Python/English Tester [My Project]/Additional Files/Image/background1.jpg);")
test_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
test_window.setWindowTitle("English-Tester")
test_window.setLayout(layout_app)
test_window.resize(1366, 768)

app.exec_()