import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lesson4.ui', self)


# Hàm hiển thị thông báo
def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Chuyển cửa sổ giao diện
def switch_window(classw):
    global window
    window = classw
    window.show()

# Run app
window = MainWindow()
window.show()
sys.exit(app.exec())

# Cách chạy file:
    # Bước 1: Chuột phải vào folder muốn chạy
    # Bước 2: Chọn "Open in integrated Terminal"
    # Bước 3: Nhập lệnh "python main.py"