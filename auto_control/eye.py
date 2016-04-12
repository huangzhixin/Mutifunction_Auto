# -*- coding: utf-8 -*-
"""
* Author：黄志新
* Create Date：2016-4-12
* Discribe : 眼睛类
"""

import urllib
import time 
import cv2
import socket

class Eye:
  def __init__(self,address):
      self.address = address
      self.html = self.GetHtml("http://"+self.address+"/index.html")
      #self.cap = cv2.VideoCapture(0)
      self.GetImg()
      img = cv2.imread('1.jpg',3)
      self.x= img.shape[1]
      self.y= img.shape[0]
      #self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
      #self.sock.connect(('192.168.10.1',9988))

      self.num=0  
      self.test=[]
      
  def GetHtml(self,url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

  def GetImg(self):
    urllib.urlretrieve("http://"+self.address+":8001/?action=snapshot","1.jpg")

  def Snapshot(self,isGary="no"):
    self.GetImg()
    if(isGary == "no"):
      img = cv2.imread('1.jpg',3)
    else:
      img = cv2.imread('1.jpg',3)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    return img

  def Display(self,isGary="no",isDetect="yes",isDispLay="yes"):
    while 1:
      img = self.Snapshot(isGary)
      """
      if(isDetect == "yes"):
        img = self.Detect(img)
        cmd=self.LockForHead(1)
        if(cmd):
          print cmd
          self.sock.send(cmd)
          print self.sock.recv(12)
      """
      if(isDispLay == "yes"):
        #cv2.circle(img,(int(0.5*self.x),int(0.5*self.y)),4,(0,255,0),2)
        cv2.imshow("Image", img)
        #print img.shape
        #print self.getResizeImage().shape
        #cv2.imshow("Image",self.getResizeImage())
        if cv2.waitKey(10) == 27:
          cv2.destroyAllWindows()
          break

  def getResizeImage(self):
      img = self.Snapshot(isGary="yes")
      resized_image = cv2.resize(img, (32,24))
      #resized_image = cv2.resize(img, int(float(img.shape)*0.1))
      return resized_image.reshape(1,resized_image.shape[0]*resized_image.shape[1])
      #return resized_image

if __name__ == "__main__":

  huang=Eye("192.168.10.1")
  huang.Display("no","yes","yes")
  #while(1):
    #print huang.LockForHead(10)

