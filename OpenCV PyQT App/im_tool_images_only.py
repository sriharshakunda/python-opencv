# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:07:07 2018

@author: Sri Harsha Kunda
If you happen to use this tool in any of your projects/research, please make sure you mentione my name in the credits.
"""

#Import libraries
import sys
import cv2
import PyQt5 as qt
import numpy as np
import cv2
import time





from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
class mainW(QMainWindow):
    def __init__(self):
        super(mainW,self).__init__()
        loadUi('im_tool.ui',self)
        self.frame=None
        self.setWindowTitle('PyQT Video Processing Tool')
    
        self.pushButton.clicked.connect(self.start)
        self.pushButton2.clicked.connect(self.stop)
        self.comboBox_2.activated.connect(self.start)
        self.comboBox_1.activated.connect(self.update_frame)
        self.comboBox_3.activated.connect(self.update_frame)
        self.checkBox.toggled.connect(self.update_frame)
        self.checkBox_2.toggled.connect(self.update_frame)
        self.checkBox_3.toggled.connect(self.update_frame)
        self.checkBox_4.toggled.connect(self.update_frame)
        self.checkBox_5.toggled.connect(self.update_frame)
        self.checkBox_5.toggled.connect(self.update_frame)
        self.dial.valueChanged.connect(self.update_frame)
        self.dial_2.valueChanged.connect(self.update_frame)
        self.dial_3.valueChanged.connect(self.update_frame)
        self.dial_4.valueChanged.connect(self.update_frame)
        self.dial_5.valueChanged.connect(self.update_frame)
        self.dial_6.valueChanged.connect(self.update_frame)
    def start(self):
        if int(self.comboBox_2.currentText())==0:
            self.cap=cv2.VideoCapture(0)
            
        elif int(self.comboBox_2.currentText())==1:
            self.cap=cv2.VideoCapture(1)
            
       
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)
    
    def sobel(self,img,orientation='x'):
        if orientation=='x':
            dst=cv2.Sobel(img, cv2.CV_64F, 1, 0)
        elif orientation=='y':
            dst=cv2.Sobel(img, cv2.CV_64F, 0, 1)
        abs_sobel = np.absolute(dst)
        scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
        return scaled_sobel
        
    def update_frame(self):
       
        self.ret,self.frame=self.cap.read()
      
        fil=str(self.comboBox_1.currentText())
        th_fil=int(self.comboBox_3.currentText())
        d_val1=self.dial.value()
        d_val2=self.dial_2.value()
        d_val3=self.dial_3.value()
        d_val4=self.dial_4.value()
        d_val5=self.dial_5.value()
        d_val6=self.dial_6.value()
   
        
        if fil=='GRAY':
            out=cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        elif fil=='HSV':
            out=cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        elif fil=='HLS':
            out=cv2.cvtColor(self.frame, cv2.COLOR_BGR2HLS)
        elif fil=='YUV':
            out=cv2.cvtColor(self.frame, cv2.COLOR_BGR2YUV)
        elif fil=='LUV':
            out=cv2.cvtColor(self.frame, cv2.COLOR_BGR2LUV)
            
        if self.checkBox.isChecked():
            self.checkBox_2.setChecked(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_3.setChecked(False)
            edges=cv2.Canny(out,d_val1,d_val1*3)
            if self.checkBox_4.isChecked():
                if self.checkBox_5.isChecked():
                    edges=self.sobel(edges,'x')+self.sobel(edges,'y')
                else:
                    edges=self.sobel(edges,'x')
            if self.checkBox_5.isChecked():
                if self.checkBox_4.isChecked():
                    edges=self.sobel(edges,'x')+self.sobel(edges,'y')
                else:
                    edges=self.sobel(edges,'y')
            final=edges
        elif self.checkBox_2.isChecked():
            self.checkBox_6.setChecked(False)
            if len(out.shape)==2:
                ret,thresh=cv2.threshold(out,d_val2,255,th_fil)
                if self.checkBox_3.isChecked():
                    thresh_cnt=cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
                    im2, contours, hierarchy = cv2.findContours(thresh_cnt,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                    for i in range(len(contours)):
                        cnt=contours[i]
                        cv2.drawContours(self.frame, [cnt], -1, (0,255,0), 3)
            elif len(out.shape)==3:
                ret,thresh=cv2.threshold(out,d_val2,255,th_fil)
                if self.checkBox_3.isChecked():
                    thresh_cnt=cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
                    im2, contours, hierarchy = cv2.findContours(thresh_cnt,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                    for i in range(len(contours)):
                        cnt=contours[i]
                        cv2.drawContours(self.frame, [cnt], -1, (0,255,0), 3)
            final=thresh
        elif self.checkBox_6.isChecked():
            self.checkBox_2.setChecked(False)
            if len(out.shape)==2:
                self.status_label_2.setText('Status: Change to 3 Channel Color Space')
                thresh=out
            elif len(out.shape)==3:
                lower_blue = np.array([d_val4,d_val5,d_val6])
                upper_blue = np.array([d_val4+10,255,255])
                mask = cv2.inRange(out, lower_blue, upper_blue)
                mask = cv2.erode(mask, None, iterations=2)
                mask = cv2.dilate(mask, None, iterations=2)
                res = cv2.bitwise_and(out,out, mask= mask)
                ret,thresh = cv2.threshold(res,d_val3,255,th_fil)
                
                if self.checkBox_3.isChecked():
                    thresh_cnt=cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
                    im2, contours, hierarchy = cv2.findContours(thresh_cnt,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                    for i in range(len(contours)):
                        cnt=contours[i]
                        cv2.drawContours(self.frame, [cnt], -1, (0,255,0), 3)
            final=thresh
        else:
            final=out
       

        self.pushButton.setDefault(False)
        self.pushButton.setAutoDefault(False)
        self.displayImage(self.frame,1)
        self.displayImage(final,2)


    
    def stop(self):
        
      
        self.timer.stop()
     
    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        
        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outImage=outImage.rgbSwapped()
        if window==1:
            self.videofeed.setPixmap(QPixmap.fromImage(outImage))
            self.videofeed.setScaledContents(True)
        elif window==2:
            self.videofeed2.setPixmap(QPixmap.fromImage(outImage))
            self.videofeed2.setScaledContents(True)

if __name__=='__main__':
    app=QApplication(sys.argv)
    widget=mainW()

    widget.show()


    sys.exit(app.exec_())