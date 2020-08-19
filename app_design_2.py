from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(60, 10, 501, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setLineWidth(1)
        self.label1.setObjectName("label1")

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "NKR_Ortho_Tool_1.v2.0"))
        self.label1.setText(_translate("MainWindow", "Outcome Prediction in proximal humerous fracture patients\n"))
        
