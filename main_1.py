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
import PySide6.QtCharts 
from formulas import dif_for_slit,dif_for_grid



class app(QMainWindow,Ui_MainWindow): 
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        self.plot = QChart()
        self.plot_2 = QChart()
        self.series = PySide6.QtCharts.QSplineSeries()
        self.series_2 = PySide6.QtCharts.QSplineSeries()
        
        self.graphicsView.viewport().installEventFilter(self)
        self.graphicsView_2.viewport().installEventFilter(self)

        self.plot.addSeries(self.series)
        self.plot_2.addSeries(self.series_2)
        
        self.pushButton.clicked.connect(self.start)  
        self.pushButton_2.clicked.connect(self.start_2) 

    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool:
        if self.graphicsView.viewport() is watched:
            print(event.pos())
            self.label_3.setText("I(x) = "+str(self.plot.mapToValue(event.pos(),self.series).x()))
            self.label_4.setText("x = "+str(self.plot.mapToValue(event.pos(),self.series).y()))
        if self.graphicsView_2.viewport() is watched:
            print(event.pos())
            self.label_7.setText("I(x) = "+str(self.plot_2.mapToValue(event.pos(),self.series_2).x()))
            self.label_6.setText("x = "+str(self.plot_2.mapToValue(event.pos(),self.series_2).y()))
        return super().eventFilter(watched, event)

    def start(self):

        
        coordinates = self.show_difract(self.lineEdit_2.text(),self.lineEdit.text())
        
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
        self.axis_y.setTitleText("Экран (x)") 
        self.axis_y.setMax(max(coordinates[0]))
        self.axis_y.setMin(-max(coordinates[0]))


        self.plot.addAxis(self.axis_y,QtCore.Qt.AlignRight)
        self.plot.setAxisX(self.axis_x, self.series)
        self.plot.setAxisY(self.axis_y, self.series)
        #self.plot.setAxisX(self.axis_x,self.candle_series)
        #self.plot.setAxisY(self.axis_y,self.candle_series) 

        #Настройка осей и и линии
        #self.plot.createDefaultAxes()
        #elf.plot.legend().hide()   
        
        
        self.plot.legend().setVisible(False)
        self.graphicsView.setMinimumWidth(330)
        #масштаб
        self.graphicsView.setRubberBand(QChartView.RectangleRubberBand)
        
        self.graphicsView.setChart(self.plot)
        self.plot.zoomReset()
    
    def start_2(self):
        
        coordinates = self.show_difract_2(self.lineEdit_5.text(),self.lineEdit_4.text(),self.lineEdit_3.text())
        
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
        self.axis_y.setTitleText("Экран (x)") 
        self.axis_y.setMax(max(coordinates[0]))
        self.axis_y.setMin(-max(coordinates[0]))


        self.plot_2.addAxis(self.axis_y,QtCore.Qt.AlignRight)
        self.plot_2.setAxisX(self.axis_x, self.series_2)
        self.plot_2.setAxisY(self.axis_y, self.series_2)

        #Настройка осей и и линии
        #self.plot.createDefaultAxes()
        #elf.plot.legend().hide()   
        
        
        self.plot_2.legend().setVisible(False)
        self.graphicsView_2.setMinimumWidth(330)
        #масштаб
        self.graphicsView_2.setRubberBand(QChartView.RectangleRubberBand)
        
        self.graphicsView_2.setChart(self.plot_2)
        self.plot_2.zoomReset()

    def show_difract(self,L,b):
        try:
            self.series.clear()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Неудалось отчистить серию")
            msg.setWindowTitle("Error")
            msg.exec_() 
        coordinates = dif_for_slit(L,b)
        for i in range(len(coordinates[0])-1,0,-1):
            
            self.series.append(coordinates[1][i],-coordinates[0][i]) 
        self.series.append(1,0)
        for i in range(0,len(coordinates[0])):
            #костыль не трогать
            if(0 == coordinates[0][i]):
                continue
                #print(-coordinates[0][i],coordinates[1][i])
            self.series.append(coordinates[1][i],coordinates[0][i])
        return coordinates 

    def show_difract_2(self,L,b,N):
        try:
            self.series.clear()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Неудалось отчистить серию")
            msg.setWind
        coordinates = dif_for_grid(L,b,N)
        print(coordinates)
        for i in range(len(coordinates[0])-1,0,-1):
            
            self.series_2.append(coordinates[1][i],-coordinates[0][i]) 
        self.series_2.append(1,0)
        for i in range(0,len(coordinates[0])):
            #костыль не трогать
            if(0 == coordinates[0][i]):
                continue
                #print(-coordinates[0][i],coordinates[1][i])
            self.series_2.append(coordinates[1][i],coordinates[0][i])
        return coordinates 


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = app()
    window.show()
    try:
        sys.exit(application.exec())
    except SystemExit:
        print("Closing Window...")