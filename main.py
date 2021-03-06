from ctypes import alignment, sizeof
import fractions
import sys
import os
import time
from traceback import walk_stack
from numpy import size
from MainWindow import Ui_MainWindow
from PySide6 import QtGui,QtCore
from PySide6.QtWidgets import QWidget,QMessageBox,QApplication,QMainWindow,QPushButton,QAbstractButton,QGraphicsView
from PySide6.QtCharts import QChart,QAbstractSeries, QSplineSeries, QChartView, QBarSeries, QBarSet, QLegend
from PySide6.QtGui import QPainter,QMouseEvent,QCursor
from PySide6.QtCore import Signal,QEvent
import PySide6.QtCharts 
from formulas import dif_for_grid, dif_for_slit




class app(QMainWindow,Ui_MainWindow): 
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        self.plot = QChart()
        self.series = PySide6.QtCharts.QSplineSeries()
        
        self.graphicsView.viewport().installEventFilter(self)
        self.graphicsView_2.viewport().installEventFilter(self)
        
        self.pushButton.clicked.connect(self.start)  
        self.pushButton_2.clicked.connect(self.start_2)

    def eventFilter(self, watched: PySide6.QtCore.QObject, event: QEvent) -> bool:
        if self.graphicsView.viewport() is watched:
            print("I(x) = "+str(self.plot.mapToValue(event.pos(),self.series).x()))
            self.label_4.setText("x = "+str(self.plot.mapToValue(event.pos(),self.series).y()))
            self.label_3.setText("I(x) = "+str(self.plot.mapToValue(event.pos(),self.series).x()))
        if self.graphicsView_2.viewport() is watched:
            self.label_7.setText("I(x) = "+str(self.plot.mapToValue(event.pos(),self.series).x()))
            self.label_6.setText("x = "+str(self.plot.mapToValue(event.pos(),self.series).y()))
        return super().eventFilter(watched, event)

    def start(self):
        self.series.clear()
        self.coordinates = self.show_difract(self.lineEdit_2.text(),self.lineEdit.text())
        
        """for i, lst in enumerate(self.coordinates):
            for data in lst:
                print(list(data))
                series.append(data[0],data[1])
            series.setName(f"{name}{i}")
            chart.addSeries(series)
        """

        # x   
        self.axis_x = PySide6.QtCharts.QValueAxis()
        self.axis_x.setTickCount(2)
        self.axis_x.setLabelFormat("%i")
        self.axis_x.setTitleText("I(x)")
        self.axis_x.setMax(1.1)
        self.axis_x.setMin(0)
        self.axis_x.setReverse(True)
        #y
        self.axis_y = PySide6.QtCharts.QValueAxis()
        self.axis_y.setTickCount(5)
        self.axis_y.setTitleText("x") 
        self.axis_y.setMax(int(2))
        self.axis_y.setMin(int(-1))


        self.plot.addAxis(self.axis_y,QtCore.Qt.AlignRight)
        self.plot.setAxisX(self.axis_x,self.series)
        self.plot.setAxisY(self.axis_y, self.series) 
        
        
        self.plot.legend().setVisible(False)
        self.graphicsView.setMinimumWidth(330)
        #??????????????
        self.graphicsView.setRubberBand(QChartView.RectangleRubberBand)
        
        self.graphicsView.setChart(self.plot)
        self.plot.zoomReset()
        
    def start_2(self):
        self.series.clear()
        
        self.coordinates = self.show_difract_2(self.lineEdit_5.text(),self.lineEdit_4.text(),self.lineEdit_3.text())
        
        # x   
        self.axis_x = PySide6.QtCharts.QValueAxis()
        self.axis_x.setTickCount(2)
        self.axis_x.setLabelFormat("%i")
        self.axis_x.setTitleText("I(x)")
        self.axis_x.setMax(1.1)
        self.axis_x.setMin(0)
        self.axis_x.setReverse(True)
        #y
        self.axis_y = PySide6.QtCharts.QValueAxis()
        self.axis_y.setTickCount(5)
        self.axis_y.setTitleText("?????????? (x)") 
        self.axis_y.setMax(max(self.coordinates[0]))
        self.axis_y.setMin(-max(self.coordinates[0]))


        self.plot.addAxis(self.axis_y,QtCore.Qt.AlignRight)
        self.plot.setAxisX(self.axis_x, self.series)
        self.plot.setAxisY(self.axis_y, self.series)

        #?????????????????? ???????? ?? ?? ??????????
        #self.plot.createDefaultAxes()
        #elf.plot.legend().hide()   
        
        
        self.plot.legend().setVisible(False)
        self.graphicsView_2.setMinimumWidth(330)
        #??????????????
        self.graphicsView_2.setRubberBand(QChartView.RectangleRubberBand)
        
        self.graphicsView_2.setChart(self.plot)
        self.plot.zoomReset()

    def show_difract(self,L,b):
        coordinates = dif_for_slit(L,b)
        m=0
        series = QSplineSeries(self.plot)
        series.append(1,0)
        #print(coordinates[1][len(coordinates[0])-1],-coordinates[0][len(coordinates[0])-1])
        series.append(0,1)
        #print(coordinates[1][len(coordinates[0])-2],-coordinates[0][len(coordinates[0])-2])
        series.append(1,0)
        #print(coordinates[1][len(coordinates[0])-3],-coordinates[0][len(coordinates[0])-3])
        self.plot.addSeries(series)
        """for i in range(len(coordinates[0])-1,0,-3):
            series = QSplineSeries(self.plot)
            series.append(coordinates[1][i],-coordinates[0][i])
            series.append(coordinates[1][i-1],-coordinates[0][i-1])
            series.append(coordinates[1][i-2],-coordinates[0][i-2])
            
            self.plot.addSeries(series)
        """self.series = QSplineSeries()
        self.series.append(0,0)        
        self.series.append(1,0)
        self.series.append(0,0)
        self.plot.addSeries(self.series)
        for i in range(0,len(coordinates[0])):
            #?????????????? ???? ??????????????
            if(0 == coordinates[0][i]):
                continue
                #print(-coordinates[0][i],coordinates[1][i])
            self.series.append(coordinates[1][i],coordinates[0][i])"""
        return coordinates 
        

    def show_difract_2(self,L,b,N):
        coordinates = dif_for_grid(L,b,N)
        
        for i in range(len(coordinates[0])-1,0,-1):
            
            self.series.append(coordinates[1][i],-coordinates[0][i]) 
        self.series.append(1,0)
        for i in range(0,len(coordinates[0])):
            #?????????????? ???? ??????????????
            if(0 == coordinates[0][i]):
                continue
                #print(-coordinates[0][i],coordinates[1][i])
            self.series.append(coordinates[1][i],coordinates[0][i])
        return coordinates 

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = app()
    window.show()
    try:
        sys.exit(application.exec())
    except SystemExit:
        print("Closing Window...")
