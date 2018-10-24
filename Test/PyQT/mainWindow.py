# coding=utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QGroupBox, QDesktopWidget, QMainWindow)



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 创建一个状态栏部件
        self.status = self.statusBar()
        # 状态栏部件添加状态信息以及设置时间(5000毫秒)
        self.status.showMessage("This is StatusBar", 5000)
        self.setWindowTitle("PyQt MianWindow")
        self.resize(600, 600)
        self.setWindowIcon(QIcon('169039.gif'))
        self.center()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Layout-Test')
        self.resize(500, 500)
        self.createLayout()

        windowLayout = QHBoxLayout()
        windowLayout.addWidget(self.testLayout)
        self.setLayout(windowLayout)


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

    def openFile(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)  # 在状态栏显示文件地址



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainWindow()
    myshow.show()
    sys.exit(app.exec_())
