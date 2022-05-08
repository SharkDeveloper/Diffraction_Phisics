# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1432, 540)
        MainWindow.setMinimumSize(QSize(1154, 495))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.page1 = QTabWidget(self.widget)
        self.page1.setObjectName(u"page1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page1.sizePolicy().hasHeightForWidth())
        self.page1.setSizePolicy(sizePolicy)
        self.page1.setMinimumSize(QSize(0, 300))
        self.page1.setMaximumSize(QSize(16777215, 16777215))
        self.Slit_page = QWidget()
        self.Slit_page.setObjectName(u"Slit_page")
        self.Slit_page.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout = QFormLayout(self.Slit_page)
        self.formLayout.setObjectName(u"formLayout")
        self.Slit = QFrame(self.Slit_page)
        self.Slit.setObjectName(u"Slit")
        self.Slit.setMinimumSize(QSize(1080, 421))
        self.Slit.setMaximumSize(QSize(16777215, 16777215))
        self.Slit.setFrameShape(QFrame.StyledPanel)
        self.Slit.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Slit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.Slit)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.Slit)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(200, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setPixmap(QPixmap(u"image/img-qo4c_Q.png"))

        self.horizontalLayout_3.addWidget(self.label_5)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.graphicsView = QChartView(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMouseTracking(True)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)

        self.verticalLayout_3.addWidget(self.graphicsView)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Slit)

        self.page1.addTab(self.Slit_page, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.tabWidgetPage2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView_2 = QChartView(self.tabWidgetPage2)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_2.addWidget(self.graphicsView_2)

        self.page1.addTab(self.tabWidgetPage2, "")

        self.gridLayout_3.addWidget(self.page1, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.page1.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 13", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0444\u0440\u0430\u043a\u0446\u0438\u044f \u043d\u0430 \u0449\u0435\u043b\u0438", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0444\u0440\u0430\u043a\u0446\u0438\u044f \u043d\u0430 \u043e\u0434\u043d\u043e\u0440\u043e\u0434\u043d\u043e\u0439 \u0440\u0435\u0448\u0435\u0442\u043a\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"L =", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043c          b(\u041d\u043c) =", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.page1.setTabText(self.page1.indexOf(self.Slit_page), QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0444\u0440\u0430\u043a\u0446\u0438\u044f \u043d\u0430 \u0449\u0435\u043b\u0438", None))
        self.page1.setTabText(self.page1.indexOf(self.tabWidgetPage2), QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0444\u0440\u0430\u043a\u0446\u0438\u044f \u043d\u0430 \u043e\u0434\u043d\u043e\u043c\u0435\u0440\u043d\u043e\u0439 \u0440\u0435\u0448\u0435\u0442\u043a\u0435", None))
    # retranslateUi

