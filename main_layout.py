from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QCoreApplication

main_line = QVBoxLayout()
start_btn = QPushButton("Start")
exit_btn = QPushButton("Quit")

start_btn.setFixedSize(260, 50)
exit_btn.setFixedSize(260, 50)

main_line.addWidget(start_btn, alignment=Qt.AlignHCenter)
main_line.addWidget(exit_btn, alignment=Qt.AlignHCenter)