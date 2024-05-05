from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
import matplotlib as pld
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QLabel
import numpy as np
from scipy.stats import norm
from scipy import stats
import statsmodels.api as sm
from PyQt5.QtWidgets import QScrollArea

class Ui_Dialog(object):
    def __init__(self,data):
        self.data=data
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(925, 662)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(9, -1, 911, 661))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.main_frame_bg = QtWidgets.QFrame(self.page)
        self.main_frame_bg.setGeometry(QtCore.QRect(-10, 0, 931, 661))
        self.main_frame_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 79, 68), stop:1 rgba(234, 103, 121));")
        self.main_frame_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_bg.setObjectName("main_frame_bg")
        self.Histogram_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.Histogram_button.setGeometry(QtCore.QRect(20, 580, 131, 41))
        self.Histogram_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"")
        self.Histogram_button.setObjectName("Histogram_button")
        self.BoxPlot_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.BoxPlot_button.setGeometry(QtCore.QRect(190, 580, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.BoxPlot_button.setFont(font)
        self.BoxPlot_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"font-family:Helvetica;")
        self.BoxPlot_button.setObjectName("BoxPlot_button")
        self.ScatterPlot_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.ScatterPlot_button.setGeometry(QtCore.QRect(370, 580, 131, 41))
        self.ScatterPlot_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"font-family:Helvetica;")
        self.ScatterPlot_button.setObjectName("ScatterPlot_button")
        self.BarPlot_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.BarPlot_button.setGeometry(QtCore.QRect(550, 580, 131, 41))
        self.BarPlot_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.BarPlot_button.setObjectName("BarPlot_button")
        self.next_1 = QtWidgets.QPushButton(self.main_frame_bg)
        self.next_1.setGeometry(QtCore.QRect(830, 580, 41, 41))
        self.next_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"")
        self.next_1.setObjectName("next_1")
        self.back = QtWidgets.QPushButton(self.main_frame_bg)
        self.back.setGeometry(QtCore.QRect(780, 580, 41, 41))
        self.back.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"")
        self.back.setObjectName("back")
        self.ProbDist_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.ProbDist_button.setGeometry(QtCore.QRect(720, 240, 191, 41))
        self.ProbDist_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.ProbDist_button.setObjectName("ProbDist_button")
        self.pushButton_8 = QtWidgets.QPushButton(self.main_frame_bg)
        self.pushButton_8.setGeometry(QtCore.QRect(740, 30, 161, 161))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        font.setUnderline(False)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame = QtWidgets.QFrame(self.main_frame_bg)
        self.frame.setGeometry(QtCore.QRect(9, -1, 701, 541))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Cholestrol_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.Cholestrol_button.setGeometry(QtCore.QRect(720, 300, 91, 41))
        self.Cholestrol_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.Cholestrol_button.setObjectName("Cholestrol_button")
        self.Trest_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.Trest_button.setGeometry(QtCore.QRect(820, 300, 91, 41))
        self.Trest_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.Trest_button.setObjectName("Trest_button")
        self.Thalach_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.Thalach_button.setGeometry(QtCore.QRect(720, 360, 91, 41))
        self.Thalach_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.Thalach_button.setObjectName("Thalach_button")
        self.OldPeak_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.OldPeak_button.setGeometry(QtCore.QRect(820, 360, 91, 41))
        self.OldPeak_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.OldPeak_button.setObjectName("OldPeak_button")
        self.Conf_int_button = QtWidgets.QPushButton(self.main_frame_bg)
        self.Conf_int_button.setGeometry(QtCore.QRect(720, 460, 191, 41))
        self.Conf_int_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.Conf_int_button.setObjectName("Conf_int_button")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tab_frame_bg = QtWidgets.QFrame(self.page_2)
        self.tab_frame_bg.setGeometry(QtCore.QRect(-11, -1, 931, 671))
        self.tab_frame_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 79, 68), stop:1 rgba(234, 103, 121));")
        self.tab_frame_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_frame_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_frame_bg.setObjectName("tab_frame_bg")
        self.Mean_frame = QtWidgets.QFrame(self.tab_frame_bg)
        self.Mean_frame.setGeometry(QtCore.QRect(40, 40, 301, 211))
        self.Mean_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.Mean_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mean_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mean_frame.setObjectName("Mean_frame")
        self.label = QtWidgets.QLabel(self.tab_frame_bg)
        self.label.setGeometry(QtCore.QRect(140, 280, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_frame_bg)
        self.label_2.setGeometry(QtCore.QRect(420, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_frame_bg)
        self.label_3.setGeometry(QtCore.QRect(700, 280, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.label_3.setObjectName("label_3")
        self.back_2 = QtWidgets.QPushButton(self.tab_frame_bg)
        self.back_2.setGeometry(QtCore.QRect(780, 580, 41, 41))
        self.back_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"")
        self.back_2.setObjectName("back_2")
        self.next_2 = QtWidgets.QPushButton(self.tab_frame_bg)
        self.next_2.setGeometry(QtCore.QRect(830, 580, 41, 41))
        self.next_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"")
        self.next_2.setObjectName("next_2")
        self.Median_frame = QtWidgets.QFrame(self.tab_frame_bg)
        self.Median_frame.setGeometry(QtCore.QRect(320, 360, 301, 211))
        self.Median_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.Median_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Median_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Median_frame.setObjectName("Median_frame")
        self.SD_frame = QtWidgets.QFrame(self.tab_frame_bg)
        self.SD_frame.setGeometry(QtCore.QRect(600, 40, 301, 211))
        self.SD_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.SD_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SD_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SD_frame.setObjectName("SD_frame")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pred_frame_bg = QtWidgets.QFrame(self.page_3)
        self.pred_frame_bg.setGeometry(QtCore.QRect(-10, 10, 931, 671))
        self.pred_frame_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 79, 68), stop:1 rgba(234, 103, 121));")
        self.pred_frame_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pred_frame_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pred_frame_bg.setObjectName("pred_frame_bg")
        self.input1_input = QtWidgets.QLineEdit(self.pred_frame_bg)
        self.input1_input.setGeometry(QtCore.QRect(50, 80, 321, 31))
        self.input1_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"box-shadow:black;")
        self.input1_input.setObjectName("input1_input")
        self.input2_input = QtWidgets.QLineEdit(self.pred_frame_bg)
        self.input2_input.setGeometry(QtCore.QRect(580, 80, 301, 31))
        self.input2_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"box-shadow:black;")
        self.input2_input.setObjectName("input2_input")
        self.pred_frame = QtWidgets.QFrame(self.pred_frame_bg)
        self.pred_frame.setGeometry(QtCore.QRect(40, 140, 691, 481))
        self.pred_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pred_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pred_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pred_frame.setObjectName("pred_frame")
        self.pred_button = QtWidgets.QPushButton(self.pred_frame_bg)
        self.pred_button.setGeometry(QtCore.QRect(770, 350, 101, 41))
        self.pred_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.pred_button.setObjectName("pred_button")
        self.input2 = QtWidgets.QPushButton(self.pred_frame_bg)
        self.input2.setGeometry(QtCore.QRect(690, 40, 101, 31))
        self.input2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.input2.setObjectName("input2")
        self.input1 = QtWidgets.QPushButton(self.pred_frame_bg)
        self.input1.setGeometry(QtCore.QRect(150, 40, 101, 31))
        self.input1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.input1.setObjectName("input1")
        self.back_3 = QtWidgets.QPushButton(self.pred_frame_bg)
        self.back_3.setGeometry(QtCore.QRect(780, 570, 41, 41))
        self.back_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"")
        self.back_3.setObjectName("back_3")
        self.next_3 = QtWidgets.QPushButton(self.pred_frame_bg)
        self.next_3.setGeometry(QtCore.QRect(830, 570, 41, 41))
        self.next_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"shadow:none;\n"
"")
        self.next_3.setObjectName("next_3")
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #all pages calls
        self.next_1.clicked.connect(self.tabPage)
        self.next_2.clicked.connect(self.predictPage)
        self.next_3.clicked.connect(self.homePage)
        self.back.clicked.connect(self.predictPage)
        self.back_2.clicked.connect(self.homePage)
        self.back_3.clicked.connect(self.tabPage)

        #making canvas
        #making layout
        self.main_Layout=QtWidgets.QHBoxLayout(self.frame)
        self.main_Layout.setObjectName("main_Layout")
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        self.main_Layout.addWidget(self.canvas) 
        #all calls for graphs
        self.Histogram_button.clicked.connect(self.histogramFun)
        self.BoxPlot_button.clicked.connect(self.boxPlotFun)
        self.ScatterPlot_button.clicked.connect(self.scatterPlotFun)
        self.BarPlot_button.clicked.connect(self.barPlotFun)
        self.Cholestrol_button.clicked.connect(self.cholProbFun)
        self.Thalach_button.clicked.connect(self.thalachProbFun)
        self.OldPeak_button.clicked.connect(self.oldpeakProbFun)
        self.Trest_button.clicked.connect(self.trestProbFun)
        self.Conf_int_button.clicked.connect(self.confFun)
        self.pred_button.clicked.connect(self.regressionFun)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Histogram_button.setText(_translate("Dialog", "Histogram"))
        self.BoxPlot_button.setText(_translate("Dialog", "Box-Plot"))
        self.ScatterPlot_button.setText(_translate("Dialog", "Scatter Plot"))
        self.BarPlot_button.setText(_translate("Dialog", "Bar Plot"))
        self.next_1.setText(_translate("Dialog", ">"))
        self.back.setText(_translate("Dialog", "<"))
        self.ProbDist_button.setText(_translate("Dialog", "Probability Distribution"))
        self.pushButton_8.setText(_translate("Dialog", "F21-9311\n"
"F21-9213\n"
"F21-9272"))
        self.Cholestrol_button.setText(_translate("Dialog", "Cholestrol"))
        self.Trest_button.setText(_translate("Dialog", "Trest BPS"))
        self.Thalach_button.setText(_translate("Dialog", "Thalach"))
        self.OldPeak_button.setText(_translate("Dialog", "Old Peak"))
        self.Conf_int_button.setText(_translate("Dialog", "Confidence Interval"))
        self.label.setText(_translate("Dialog", "   Mean "))
        self.label_2.setText(_translate("Dialog", "  Median  "))
        self.label_3.setText(_translate("Dialog", "    S.D  "))
        self.back_2.setText(_translate("Dialog", "<"))
        self.next_2.setText(_translate("Dialog", ">"))
        self.pred_button.setText(_translate("Dialog", "Prediction"))
        self.input2.setText(_translate("Dialog", "Thalach"))
        self.input1.setText(_translate("Dialog", "Cholestrol"))
        self.back_3.setText(_translate("Dialog", "<"))
        self.next_3.setText(_translate("Dialog", ">"))
    def homePage(self):
        self.stackedWidget.setCurrentWidget(self.page)
    def tabPage(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.mean1()
    def predictPage(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
    #making all graphs
    def histogramFun(self):
        self.figure.clear()
        chol_col=self.data['chol']
        min_chol = min(chol_col)
        max_chol = max(chol_col)
        num_intervals = 7
        interval_width = (max_chol - min_chol) / num_intervals
        intervals = [min_chol + i * interval_width for i in range(num_intervals)]
        intervals.append(max_chol)
        plt.hist(chol_col, bins=intervals, edgecolor='black',color='red')
        plt.xlabel(' cholestoral (mg/dl)')
        plt.ylabel('Persons')
        plt.title('Cholestrol Level in Patients')
        self.canvas.draw()
    def boxPlotFun(self):

        self.figure.clear()
        age_col=self.data['age']
        plt.boxplot(age_col,vert=False)
        plt.title('Box Plot of Age')
        plt.xlabel('Age')
        self.canvas.draw()
    def scatterPlotFun(self):
       
        self.figure.clear()
        Age_col = self.data['age']
        Chol_col = self.data['chol']
        plt.scatter(Age_col, Chol_col, label='Cholestrol')

        trestbps_col = self.data['trestbps']
        thalach_col = self.data['thalach']
        plt.scatter(trestbps_col, thalach_col, label='Thalach')

        oldpeak_col = self.data['oldpeak']
        plt.scatter(oldpeak_col, thalach_col, label='Oldpeak')

        plt.scatter(Age_col, trestbps_col, label='Trestbps')

        plt.xlabel('Age')
        plt.ylabel('Values')
        plt.legend()
        plt.tight_layout()
        plt.grid(True)
        self.canvas.draw()
    def barPlotFun(self):
        self.figure.clear()
               # Frequency of different chest pain types (cp)
        plt.subplot(221)
        self.data['cp'].value_counts().sort_index().plot(kind='bar', color='skyblue')
        plt.xlabel('Chest Pain Type')


        # Distribution of resting electrocardiographic results (restecg)
        plt.subplot(222)
        self.data['restecg'].value_counts().sort_index().plot(kind='bar', color='salmon')
        plt.xlabel('Resting Electrocardiographic Result')


        # Frequency of different values of ca (number of major vessels colored by fluoroscopy)
        plt.subplot(223)
        self.data['ca'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
        plt.xlabel('CA Value')
      

        # Distribution of thal values
        plt.subplot(224)
        self.data['thal'].value_counts().sort_index().plot(kind='bar', color='gold')
        plt.xlabel('Thal Value')
      

        plt.tight_layout()
        self.canvas.draw()
    def cholProbFun(self):
        self.figure.clear()
        chol_col=self.data['chol']
        mean_chol,std_dev_chol=norm.fit(chol_col)
        min_trest = min(chol_col)
        max_trest = max(chol_col)
        num_intervals = 7
        interval_width = (max_trest - min_trest) / num_intervals
        intervals = [min_trest + i * interval_width for i in range(num_intervals)]
        intervals.append(max_trest)
       # Plot histogram of the original data
        plt.hist(chol_col, bins=intervals, density=True, alpha=0.6, color='pink')
        # Plot the PDF of the fitted normal distribution
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean_chol, std_dev_chol)
        plt.plot(x, p, 'k', linewidth=2)
        plt.xlabel('Cholestrol',fontsize=7)
        plt.ylabel('Density',fontsize=7)
        plt.title('Normal Distribution to Cholestrol',fontsize=10)
        self.canvas.draw()
    def trestProbFun(self):
        self.figure.clear()
        trestbps_col=self.data['trestbps']
        mean_trest,std_dev_trest=norm.fit(trestbps_col)
        min_trest = min(trestbps_col)
        max_trest = max(trestbps_col)
        num_intervals = 7
        interval_width = (max_trest - min_trest) / num_intervals
        intervals = [min_trest + i * interval_width for i in range(num_intervals)]
        intervals.append(max_trest)
       # Plot histogram of the original data
        plt.hist(trestbps_col, bins=intervals, density=True, alpha=0.6, color='g')
        # Plot the PDF of the fitted normal distribution
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean_trest, std_dev_trest)
        plt.plot(x, p, 'k', linewidth=2)
        plt.xlabel('trestbps',fontsize=7)
        plt.ylabel('Density',fontsize=7)
        plt.title('Distribution to trestbps',fontsize=10)
        self.canvas.draw()
    def thalachProbFun(self):
        self.figure.clear()
        chol_col=self.data['thalach']
        mean_chol,std_dev_chol=norm.fit(chol_col)
        min_trest = min(chol_col)
        max_trest = max(chol_col)
        num_intervals = 7
        interval_width = (max_trest - min_trest) / num_intervals
        intervals = [min_trest + i * interval_width for i in range(num_intervals)]
        intervals.append(max_trest)
       # Plot histogram of the original data
        plt.hist(chol_col, bins=intervals, density=True, alpha=0.6, color='r')
        # Plot the PDF of the fitted normal distribution
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean_chol, std_dev_chol)
        plt.plot(x, p, 'k', linewidth=2)
        plt.xlabel('Max Heart Rate',fontsize=7)
        plt.ylabel('Density',fontsize=7)
        plt.title('Normal Distribution to Thalach',fontsize=10)
        self.canvas.draw()
    def oldpeakProbFun(self):
        self.figure.clear()
        chol_col=self.data['oldpeak']
        mean_chol,std_dev_chol=norm.fit(chol_col)
        min_trest = min(chol_col)
        max_trest = max(chol_col)
        num_intervals = 7
        interval_width = (max_trest - min_trest) / num_intervals
        intervals = [min_trest + i * interval_width for i in range(num_intervals)]
        intervals.append(max_trest)
       # Plot histogram of the original data
        plt.hist(chol_col, bins=intervals, density=True, alpha=0.6, color='r')
        # Plot the PDF of the fitted normal distribution
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean_chol, std_dev_chol)
        plt.plot(x, p, 'k', linewidth=2)
        plt.xlabel('ST Depression induced by exercise relative to rest',fontsize=7)
        plt.ylabel('Density',fontsize=7)
        plt.title('Normal Distribution to Oldpeak',fontsize=10)
        self.canvas.draw()
    def calculate_confidence_interval(self,data):
        confidence_level=0.95
        mean = data['mean']
        std_dev = data['std']
        sample_size = data['count']
        margin_of_error = stats.norm.ppf(1 - (1 - confidence_level) / 2) * (std_dev / (sample_size ** 0.5))
        confidence_interval_lower = mean - margin_of_error
        confidence_interval_upper = mean + margin_of_error
        return confidence_interval_lower, confidence_interval_upper
    def confFun(self):
        self.figure.clear()
        variables_of_interest = ['chol', 'thalach', 'trestbps', 'fbs', 'oldpeak']

        # Calculate descriptive statistics for the specified variables
        descriptive_stats = self.data[variables_of_interest].describe()

        confidence_intervals = {}
        for variable in variables_of_interest:
                confidence_intervals[variable] = self.calculate_confidence_interval(descriptive_stats[variable])

        # Create a subplot within the canvas
        ax = self.figure.add_subplot(111)

        for i, variable in enumerate(variables_of_interest):
                interval = confidence_intervals[variable]
                ax.hist(self.data[variable], bins=20, alpha=0.5, label=variable)
                ax.axvline(x=descriptive_stats.loc['mean', variable], color='r', linestyle='--', label='Mean')
                ax.axvline(x=interval[0], color='g', linestyle=':', label='Lower CI')
                ax.axvline(x=interval[1], color='g', linestyle=':', label='Upper CI')
                ax.set_ylabel('Frequency')
                ax.set_title(f'Histogram of {variable} with Confidence Intervals')
                ax.legend(fontsize=7)
                

               #line to be deleted
                print(f'Confidence Interval for {variable}: [{interval[0]:.2f}, {interval[1]:.2f}]')

        self.canvas.draw()
    def mean1(self):
        male_data = self.data[self.data['sex'] == 1]
        female_data = self.data[self.data['sex'] == 0]
        male_age_avg =round( np.mean(male_data['age']),5)
        female_age_avg = round(np.mean(female_data['age']),5)
        oa_chol = round(np.mean(self.data['chol']),5)  
        oa_thalach=round(np.mean(self.data['thalach']),5)
        od_oldpeak=round(np.mean(self.data['oldpeak']),5)
        fbs_count = pd.Series(self.data['fbs'])[1]
        trg_count = pd.Series(self.data['target'])[1]
        male_var=round(np.var(male_data['age']),5)
        female_var=round(np.var(female_data['age']),5)
        oa_chol_var=round(np.var(self.data['chol']),2)
        oa_thalach_var=round(np.var(self.data['thalach']),5)
        od_oldpeak_var=round(np.var(self.data['oldpeak']),5)
        male_sd=round(np.sqrt(male_var),5)
        female_sd=round(np.sqrt(female_var),5)
        oa_chol_sd=round(np.sqrt(oa_chol_var),5)
        oa_thalach_sd=round(np.sqrt(oa_thalach_var),5)
        oa_oldpeak_sd=round(np.sqrt(od_oldpeak_var),5)
        mean_label=QLabel(f"Male Age Average : {male_age_avg} \nFemale Age Average : {female_age_avg}\nAverage Cholestrol Level : {oa_chol}\n Average Thalach : {oa_thalach} \nAverage Oldpeak : {od_oldpeak}")
        var_label=QLabel(f"Male Age Variance : {male_var} \nFemale Age Variance : {female_var}\nVariance Cholestrol Level : {oa_chol_var}\nVariance Thalach : {oa_thalach_var} \nVariance Oldpeak : {od_oldpeak_var} ")
        sd_label=QLabel(f"Male Age SD : {male_sd} \nFemale Age SD : {female_sd}\nCholestrol SD : {oa_chol_sd}\nThalach SD : {oa_thalach_sd} \nOldpeak SD : {oa_oldpeak_sd} ")
        layout=QtWidgets.QVBoxLayout(self.Mean_frame)
        layout.addWidget(mean_label)
        layout1=QtWidgets.QVBoxLayout(self.Median_frame)
        layout1.addWidget(var_label)
        layout2=QtWidgets.QVBoxLayout(self.SD_frame)
        layout2.addWidget(sd_label)
    def regressionFun(self):
        try:
            # Load data from Excel file

            # Split data into independent (X) and dependent (y) variables
            X = self.data[['chol', 'thalach']]  # Use 'chol' and 'thalach' as independent variables
            y = self.data['target']

            # Add constant term for intercept
            X = sm.add_constant(X)

            # Train the model
            model = sm.OLS(y, X).fit()

            # Prompt user for input
            chol_input = self.input1_input.text()
            thalach_input = self.input2_input.text()

            if chol_input.isdigit() and thalach_input.isdigit():
                chol = float(chol_input)
                thalach = float(thalach_input)
                # Make prediction
                user_input = np.array([[1, chol, thalach]])  # Adding constant term manually
                prediction = model.predict(user_input)

                # Display prediction and model summary
                prediction_text = f"Predicted likelihood of heart disease: {prediction[0]} \n\nModel Summary:\n{model.summary()}"
                prediction_label = QtWidgets.QLabel(prediction_text)
            else:
                prediction_label = QtWidgets.QLabel("Enter float values")

            # Create a scroll area
            scroll_area = QtWidgets.QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(prediction_label)

            # Clear previous layout
            self.pred_frame.setLayout(QtWidgets.QHBoxLayout())

            # Add the scroll area to the layout
            self.pred_frame.layout().addWidget(scroll_area)

        except Exception as e:
            err_label = QtWidgets.QLabel("Some error Occurred!!!")
            # Clear previous layout
            self.pred_frame.setLayout(QtWidgets.QHBoxLayout())
            self.pred_frame.layout().addWidget(err_label)



if __name__ == "__main__":
    data=pd.read_excel('heart-disease.xlsx')
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(data=data)
    ui.setupUi(Dialog)
    Dialog.show()
    ui.homePage()
    sys.exit(app.exec_())
