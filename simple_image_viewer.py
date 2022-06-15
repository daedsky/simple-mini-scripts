from PyQt5 import QtCore, QtGui, QtWidgets
import os

pictures_folder_path = f'c://users/{os.getlogin()}/Pictures/' if os.name == 'nt' else f'/home/{os.getlogin()}/Pictures/'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.previous_btn = QtWidgets.QPushButton(self.centralwidget)
        self.previous_btn.setGeometry(QtCore.QRect(0, 530, 75, 23))
        self.previous_btn.setObjectName("previous_btn")
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(720, 530, 75, 23))
        self.next_btn.setObjectName("next_btn")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(""))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.image.raise_()
        self.previous_btn.raise_()
        self.next_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.next_btn.clicked.connect(self.next_image)
        self.previous_btn.clicked.connect(self.previous_imgae)

        self.counter = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.previous_btn.setText(_translate("MainWindow", "previous"))
        self.next_btn.setText(_translate("MainWindow", "next"))

    def next_image(self):
        self.path = pictures_folder_path
        self.all_files = os.listdir(self.path)

        self.all_photos = []

        self.dirs = []

        for file in self.all_files:
            if os.path.isdir(os.path.join(self.path, file)):
                self.dirs.append(os.path.join(self.path, file))
            else:
                self.all_photos.append(os.path.join(self.path, file))

        def rec(dir_path):
            for file in os.listdir(dir_path):
                full_path = os.path.join(dir_path, file)
                if os.path.isdir(full_path):
                    self.dirs.append(full_path)
                else:
                    self.all_photos.append(full_path)

        for folder in self.dirs:
            files = os.listdir(folder)
            for file in files:
                fp = os.path.join(folder, file)
                if os.path.isdir(fp):
                    rec(fp)
                else:
                    self.all_photos.append(fp)

        if self.counter < (len(self.all_photos) - 1):
            self.counter += 1

            self.image.setPixmap(QtGui.QPixmap(self.all_photos[self.counter]))
            # print(self.all_photos[self.counter] + "counter is: " + str(self.counter))

    def previous_imgae(self):
        if self.counter > 0:
            self.counter -= 1
            self.image.setPixmap(QtGui.QPixmap(self.all_photos[self.counter]))
            # print(self.all_photos[self.counter] + "counter is: " + str(self.counter))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle("photo viewer")
    # MainWindow.setWindowIcon(QtGui.QIcon(r"icon.png"))

    sys.exit(app.exec_())
