
from PyQt4 import QtCore, QtGui
import crypt_engine

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
key = 2
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(636, 445)
        MainWindow.setMinimumSize(QtCore.QSize(636, 445))
        MainWindow.setMaximumSize(QtCore.QSize(636, 445))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 391))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 5, 0, 1, 5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.encryptBtn = QtGui.QPushButton(self.layoutWidget)
        self.encryptBtn.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.encryptBtn, 0, 0, 1, 1)
        self.decryptBtn = QtGui.QPushButton(self.layoutWidget)
        self.decryptBtn.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.decryptBtn, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 0, 1, 5)
        self.textEdit_2 = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_2.addWidget(self.textEdit_2, 7, 0, 1, 5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 3, 1, 1)
        self.layoutLbl = QtGui.QLabel(self.layoutWidget)
        self.layoutLbl.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.layoutLbl, 1, 0, 1, 1)
        self.keyLbl = QtGui.QLabel(self.layoutWidget)
        self.keyLbl.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.keyLbl, 3, 0, 1, 1)
        self.enRBtn = QtGui.QRadioButton(self.layoutWidget)
        self.enRBtn.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_2.addWidget(self.enRBtn, 1, 1, 1, 1)
        self.ruRBtn = QtGui.QRadioButton(self.layoutWidget)
        self.ruRBtn.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_2.addWidget(self.ruRBtn, 1, 3, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox.setEnabled(True)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(26)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_2.addWidget(self.spinBox, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.maxKeyLbl = QtGui.QLabel(self.layoutWidget)
        self.maxKeyLbl.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.maxKeyLbl, 3, 2, 1, 1)
        self.confirmBtn = QtGui.QPushButton(self.layoutWidget)
        self.confirmBtn.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.confirmBtn, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифратор", None))
        self.encryptBtn.setText(_translate("MainWindow", "Зашифровать", None))
        self.encryptBtn.connect(self.encryptBtn, QtCore.SIGNAL('clicked()'),
                                self.encryptText)
        self.decryptBtn.setText(_translate("MainWindow", "Расшифровать", None))
        self.decryptBtn.connect(self.decryptBtn, QtCore.SIGNAL('clicked()'),
                                self.decryptText)
        self.layoutLbl.setText(_translate("MainWindow",
                                          "Укажите вашу раскладку:", None))
        self.keyLbl.setText(_translate("MainWindow", "Укажите длину ключа:",
                                       None))
        self.enRBtn.setText(_translate("MainWindow", "EN", None))
        self.enRBtn.setChecked(True)
        self.enRBtn.connect(self.enRBtn, QtCore.SIGNAL('clicked()'),
                            self.changeKeyMax)
        self.ruRBtn.setText(_translate("MainWindow", "RU", None))
        self.ruRBtn.connect(self.ruRBtn, QtCore.SIGNAL('clicked()'),
                            self.changeKeyMax)
        self.maxKeyLbl.setText(_translate("MainWindow",
                                          "(Максимальная длина - 25)   --->",
                                          None))
        self.confirmBtn.setText(_translate("MainWindow", "Подтвердить", None))
        self.confirmBtn.connect(self.confirmBtn, QtCore.SIGNAL('clicked()'),
                                self.setKey)

    def encryptText(self):
        if self.enRBtn.isChecked():
            text = self.textEdit.toPlainText()
            crypt_text = crypt_engine.encrypt(text, crypt_engine.En,
                                              crypt_engine.alphabetEn, key)
            self.textEdit_2.setText(crypt_text)
        elif self.ruRBtn.isChecked():
            text = self.textEdit.toPlainText()
            crypt_text = crypt_engine.encrypt(text, crypt_engine.Ru,
                                              crypt_engine.alphabetRu, key)
            self.textEdit_2.setText(crypt_text)

    def decryptText(self):
        if self.enRBtn.isChecked():
            text = self.textEdit.toPlainText()
            encrypt_text = crypt_engine.decrypt(text, crypt_engine.En,
                                                crypt_engine.alphabetEn, key)
            self.textEdit_2.setText(encrypt_text)
        elif self.ruRBtn.isChecked():
            text = self.textEdit.toPlainText()
            encrypt_text = crypt_engine.decrypt(text, crypt_engine.Ru,
                                                crypt_engine.alphabetRu, key)
            self.textEdit_2.setText(encrypt_text)

    def changeKeyMax(self):
        if self.enRBtn.isChecked():
            self.maxKeyLbl.setText("(Максимальная длина - 25)   --->")
            self.spinBox.setMaximum(25)
        else:
            self.maxKeyLbl.setText("(Максимальная длина - 45)   --->")
            self.spinBox.setMaximum(45)

    def setKey(self):
        global key
        key = self.spinBox.value()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())