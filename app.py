from scraper import scrape
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(463, 386)
                self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
                self.centralwidget.setStyleSheet("background-color: rgb(33,33,33);\n"
        "color: #ffffff")
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.codeArea = QtWidgets.QTextEdit(parent=self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Ubuntu Mono")
                font.setPointSize(18)
                self.codeArea.setFont(font)
                self.codeArea.setStyleSheet("background-color: rgb(46,46,46);\n"
        "color: #ffffff")
                self.codeArea.setObjectName("codeArea")
                self.gridLayout.addWidget(self.codeArea, 2, 0, 5, 1)
                self.scrapeButton = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda:self.scrapeClicked())
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(14)
                self.scrapeButton.setFont(font)
                self.scrapeButton.setStyleSheet("background-color: rgb(25,25,25)")
                self.scrapeButton.setObjectName("scrapeButton")
                self.gridLayout.addWidget(self.scrapeButton, 1, 0, 1, 2)
                self.problemDisplay = QtWidgets.QTextBrowser(parent=self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.problemDisplay.setFont(font)
                self.problemDisplay.setStyleSheet("background-color: rgb(46,46,46);\n"
        "color: #ffffff")
                self.problemDisplay.setObjectName("problemDisplay")
                self.gridLayout.addWidget(self.problemDisplay, 5, 1, 1, 1)
                self.searchBox = QtWidgets.QLineEdit(parent=self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(14)
                self.searchBox.setFont(font)
                self.searchBox.setStyleSheet("background-color: rgb(46,46,46);\n"
        "color: #ffffff")
                self.searchBox.setObjectName("searchBox")
                self.gridLayout.addWidget(self.searchBox, 0, 0, 1, 2)
                self.problemTitle = QtWidgets.QLabel(parent=self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.problemTitle.setFont(font)
                self.problemTitle.setStyleSheet("background-color: rgb(46,46,46);\n"
        "font: 75 16pt \"Times New Roman\";\n"
        "color: #ffffff;")
                self.problemTitle.setText("")
                self.problemTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.problemTitle.setObjectName("problemTitle")
                self.gridLayout.addWidget(self.problemTitle, 2, 1, 3, 1, QtCore.Qt.AlignmentFlag.AlignVCenter)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def scrapeClicked(self):
               q = self.searchBox.text()
               response = scrape(q)
               self.problemTitle.setText(response["title"])
               self.problemDisplay.setText(response["content"]+"\nInput:\n"+response["input_specs"]+"\nOutput:\n"+response["output_specs"])

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.scrapeButton.setText(_translate("MainWindow", "scrape"))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
