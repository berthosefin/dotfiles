# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hello_worldGsZMeg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HelloWorld(object):
    def setupUi(self, HelloWorld):
        if not HelloWorld.objectName():
            HelloWorld.setObjectName(u"HelloWorld")
        HelloWorld.resize(356, 221)
        self.centralwidget = QWidget(HelloWorld)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 271, 141))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(False)

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        HelloWorld.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(HelloWorld)
        self.statusbar.setObjectName(u"statusbar")
        HelloWorld.setStatusBar(self.statusbar)

        self.retranslateUi(HelloWorld)

        QMetaObject.connectSlotsByName(HelloWorld)
    # setupUi

    def retranslateUi(self, HelloWorld):
        HelloWorld.setWindowTitle(QCoreApplication.translate("HelloWorld", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("HelloWorld", u"Hello World", None))
        self.pushButton.setText(QCoreApplication.translate("HelloWorld", u"OK", None))
    # retranslateUi

