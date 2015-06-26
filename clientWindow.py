# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Mon Jun 22 17:25:55 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from drawArea import GridArea, GridView
from elements import Grid
from client import Client
from settings import Settings

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(752, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.connectButton = QtGui.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(590, 10, 151, 71))
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.disconnectButton = QtGui.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(590, 90, 151, 71))
        self.disconnectButton.setObjectName(_fromUtf8("disconnectButton"))
        
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(670, 170, 71, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 170, 71, 16))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.settings = Settings()
        self.client = Client(self.settings,self)
        self.grid = Grid(self.settings)
        self.gridArea = GridArea(self.settings,self.grid)
        self.gridView = GridView(self.settings,self.centralwidget,self.gridArea,self.client)     
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.client.connect)
        QtCore.QObject.connect(self.disconnectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.client.disconnect)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL(_fromUtf8("redraw")), self.gridView.drawGrid)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL(_fromUtf8("change")), self.gridView.changeAtom)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ClientWindow", None))
        self.connectButton.setText(_translate("MainWindow", "Connect", None))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect", None))
        self.lineEdit.setText(_translate("MainWindow", "2323", None))
        self.label.setText(_translate("MainWindow", "Port n°", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    app.setActiveWindow(MainWindow)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

