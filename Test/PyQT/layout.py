# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QGroupBox, QDesktopWidget, QMainWindow)


class pyqt5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Layout-Test')
        self.center()
        self.resize(500, 500)
        self.setWindowIcon(QIcon('169039.gif'))
        self.createLayout()



        windowLayout = QHBoxLayout()
        windowLayout.addWidget(self.testLayout)
        self.setLayout(windowLayout)

        self.show()

    # 展示在屏幕中心的代码
    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 展示到屏幕中心
        self.move(qr.topLeft())

    def createLayout(self):
        self.testLayout = QGroupBox('这是一个测试GroupBox的案例')

        regist_btn = QPushButton('注册', self)
        regist_btn.clicked.connect(self.onClick)
        login_btn = QPushButton('登陆', self)
        test_btn = QPushButton('测试', self)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(login_btn)
        hbox1.addStretch(1)
        hbox1.addWidget(regist_btn)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(test_btn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.testLayout.setLayout(vbox)

    def onClick(self):
        reply = self.sender()
        self.statusBar().showMessage('假装你已经' + reply.text() + '了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pyqt5()
    sys.exit(app.exec_())



