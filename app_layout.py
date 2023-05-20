from PyQt5.QtWidgets import QApplication, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QGroupBox, QButtonGroup
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from data import *

def squestion():
    btn_group.setExclusive(False)
    for b in btn_list:
        b.setChecked(False)
    btn_group.setExclusive(True)
    group_box2.hide()
    group_box.show()
    answer_btn.setText("Answer")

def sresult():
    head_lb.hide()
    play_lb.hide()
    group_box.hide()
    group_box2.show()
    answer_btn.setText("Next Question")

app = QApplication([])

head_lb = QLabel("Press '<b>Play Audio</b>' to listen to the sentence, and select the said sentence from the answer options")
group_box = QGroupBox("Answer Options")
group_box2 = QGroupBox("Test Result")
play_lb = QPushButton("Play Audio")
answer_btn = QPushButton("Answer")
result = QLabel("Right/Wrong")
menu_btn = QPushButton("Menu")
result_answ = QLabel("Result")

layout_group2 = QVBoxLayout()
layout_group = QHBoxLayout()
line_group3 = QVBoxLayout()
line_group2 = QVBoxLayout()
line_group = QVBoxLayout()
layout_app = QVBoxLayout()
btn_group = QButtonGroup()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

btn_list = []
for i in range(6):
    btn = QRadioButton("")
    btn_list.append(btn)
    btn_group.addButton(btn)
    btn.setStyleSheet("background: rgb();")

line_group.addWidget(btn_list[0])
line_group.addWidget(btn_list[1])
line_group2.addWidget(btn_list[2])
line_group2.addWidget(btn_list[3])
line_group3.addWidget(btn_list[4])
line_group3.addWidget(btn_list[5])

layout_group.addLayout(line_group)
layout_group.addLayout(line_group2)
layout_group.addLayout(line_group3)
group_box.setLayout(layout_group)

layout_group2.addWidget(result, alignment=Qt.AlignTop | Qt.AlignHCenter)
layout_group2.addStretch(1)
layout_group2.addWidget(result_answ, alignment=Qt.AlignHCenter)
layout_group2.addStretch(1)

group_box2.setLayout(layout_group2)
group_box2.hide()

line2.addStretch(1)
line2.addWidget(answer_btn, stretch=2)
line2.addWidget(menu_btn, stretch=2)
line2.addStretch(1)

layout_app.addLayout(line1)
layout_app.addStretch(1)
layout_app.addWidget(head_lb, alignment=Qt.AlignHCenter)
layout_app.addStretch(1)
layout_app.addWidget(play_lb, alignment=Qt.AlignHCenter)
layout_app.addStretch(1)
layout_app.addWidget(group_box, stretch=13)
layout_app.addWidget(group_box2, stretch=13)
layout_app.addStretch(1)
layout_app.addLayout(line2)
layout_app.addStretch(1)