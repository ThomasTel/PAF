# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
		
class Atom:
    def __init__(self,i,j,state=0):
        self.i=i
        self.j=j
        self.state=state

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 571, 581))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.drawButton = QtGui.QPushButton(self.centralwidget)
        self.drawButton.setGeometry(QtCore.QRect(590, 10, 201, 61))
        self.drawButton.setObjectName(_fromUtf8("drawButton"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 80, 201, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.spinHeight = QtGui.QSpinBox(self.centralwidget)
        self.spinHeight.setGeometry(QtCore.QRect(700, 150, 91, 22))
        self.spinHeight.setObjectName(_fromUtf8("spinHeight"))
        self.spinWidth = QtGui.QSpinBox(self.centralwidget)
        self.spinWidth.setGeometry(QtCore.QRect(590, 150, 91, 22))
        self.spinWidth.setObjectName(_fromUtf8("spinWidth"))
        self.scene = QtGui.QGraphicsScene(0,0,571,581,self.graphicsView)
        self.graphicsView.setScene(self.scene)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.drawButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.drawSomething)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.drawCells)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.drawButton.setText(_translate("MainWindow", "Big Button", None))
        self.pushButton.setText(_translate("MainWindow", "drawCells", None))
    def drawSomething(self):
        self.scene.addText("EREVEV")
        self.graphicsView.show()
    def drawCells(self):
        h,w = self.spinHeight.value(),self.spinWidth.value()
        for i in range(h):
            for j in range(w):
                self.scene.addRect(10*i+1,10*j+1,8,8)
        self.graphicsView.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

