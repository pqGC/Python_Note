import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow


class PyQT5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()  # 初始化界面

    def initUI(self):
        # self.setGeometry(700, 200, 500, 500)  # 设置窗口位置和大小
        self.resize(500, 500)
        self.center()
        self.setWindowTitle('PyQT5')  # 设置窗口标题
        self.setWindowIcon(QIcon('169039.gif'))  # 设置应用图标
        QToolTip.setFont(QFont('ScanSerif', 10))  # 提示字体 10px滑体字体
        # self.setToolTip('This is a <b>QWidget</b> widget')  # 可使用富文本格式

        btn = QPushButton('注册', self)
        btn.setToolTip('<b>假装</b>是个注册按钮')  # 创建一个btn 并为他设置提示文字
        btn.resize(100, 35)  # 设置按钮的大小
        btn.move(400, 0)  # 设置按钮位置
        btn.clicked.connect(self.onClick)

        quit_btn = QPushButton('EXIT', self)  # 自定义一个退出按钮
        quit_btn.resize(100, 35)
        quit_btn.move(400, 465)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        # quit_btn.clicked.connect(self.closeEvent)
        self.statusBar()
        self.show()

    def onClick(self):
        reply = self.sender()
        self.statusBar().showMessage('假装你已经' + reply.text() + '了')

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'message', '你确定要退出吗？',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    # 展示在屏幕中心的代码
    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 展示到屏幕中心
        self.move(qr.topLeft())


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    exe = PyQT5()
    sys.exit(app.exec_())



