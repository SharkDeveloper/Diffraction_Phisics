
from ctypes import alignment, sizeof
import fractions
import sys
import os
import time
from numpy import size
from pandas import Series
from MainWindow import Ui_MainWindow
from PySide6 import QtGui,QtCore
from PySide6.QtWidgets import QWidget,QMessageBox,QApplication,QMainWindow,QPushButton,QAbstractButton
from PySide6.QtCharts import QChart,QAbstractSeries, QSplineSeries, QChartView, QBarSeries, QBarSet, QLegend, QBarCategoryAxis
from PySide6.QtGui import QPainter
import PySide6.QtCharts 
from formulas import dif_for_slit

class app(Ui_MainWindow):
    def __init__(self,MainWindow) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.plot = QChart()
        self.series = PySide6.QtCharts.QSplineSeries()
        self.candle_series =  PySide6.QtCharts.QCandlestickSeries()
        self.plot.addSeries(self.series)
        self.plot.addSeries(self.candle_series)

        #self.plot.createDefaultAxes()
        #elf.plot.legend().hide()   
        # x   
        self.axis_x = PySide6.QtCharts.QValueAxis()
        self.axis_x.setTickCount(10)
        self.axis_x.setLabelFormat("%i")
        self.axis_x.setTitleText("Экран (x)")
        self.axis_x.setMax(10)
        self.axis_x.setMin(-10)
        #y
        self.axis_y = PySide6.QtCharts.QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setTitleText("I(x)")
        self.axis_y.setMax(1)
        self.axis_y.setMin(0)
        self.axis_y.setReverse(True)


        self.plot.addAxis(self.axis_x,QtCore.Qt.AlignRight)
        #self.plot.addAxis(self.axis_y,QtCore.Qt.Align)
        self.plot.setAxisY(self.axis_x, self.series)
        self.plot.setAxisX(self.axis_y, self.series)
        self.plot.setAxisY(self.axis_x,self.candle_series)
        self.plot.setAxisX(self.axis_y,self.candle_series) 

        
        
        self.plot.legend().setVisible(False)
        self.graphicsView.setMinimumWidth(330)
        #масштаб
        #self.graphicsView.setRubberBand(QChartView.)

        #
        self.graphicsView.setChart(self.plot)
        self.pushButton.clicked.connect(self.start)
                
                
       
    def start(self):
        self.show_difract(self.lineEdit_2.text(),self.lineEdit.text())

    def show_difract(self,L,b):
        coordinates = dif_for_slit(L,b)
        for i in range(0,size(coordinates[0])):
            if i%2 == 0:
                print(0,float(coordinates[0][i]))
                self.series.append(0,float(coordinates[0][i]))
            else:
                count = int(i/2)
                print(coordinates[1][count],coordinates[0][i])
                self.series.append(coordinates[1][count],coordinates[0][i])   
        

if __name__ == "__main__":
    application= QApplication(sys.argv)

    mw=QMainWindow()
    a=app(mw)
    mw.show()
    
    try:
        sys.exit(application.exec())
    except SystemExit:
        print("Closing Window...")
