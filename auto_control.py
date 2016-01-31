# -*- coding:utf-8 -*-  
import RPi.GPIO as gpio
import time
class Auto:
  def __init__(self,wheels):
    self.allwheels=wheels
    self.rightwheel=wheels[0:2]
    self.leftwheel=wheels[2:4]
    self.pwm=wheels[4:6]
    print self.rightwheel ,self.leftwheel, self.pwm
    gpio.setmode(gpio.BOARD)
    for port in wheels:
      gpio.setup(port,gpio.OUT)
    self.p1=gpio.PWM(self.pwm[0], 50)
    self.p2=gpio.PWM(self.pwm[1], 50)
    self.nowspeed=30
    self.p1.start(self.nowspeed)
    self.p2.start(self.nowspeed)
  
  def stop(self):
    for port in self.allwheels:
      gpio.output(port,gpio.LOW)
 
  def forward(self):
      gpio.output(self.allwheels[0],gpio.HIGH)
      gpio.output(self.allwheels[1],gpio.LOW)
      gpio.output(self.allwheels[2],gpio.HIGH)
      gpio.output(self.allwheels[3],gpio.LOW)

  def backward(self):
      gpio.output(self.allwheels[0],gpio.LOW)
      gpio.output(self.allwheels[1],gpio.HIGH)
      gpio.output(self.allwheels[2],gpio.LOW)
      gpio.output(self.allwheels[3],gpio.HIGH)
  
  def turnright(self):
      gpio.output(self.allwheels[0],gpio.LOW)
      gpio.output(self.allwheels[1],gpio.HIGH)
      gpio.output(self.allwheels[2],gpio.HIGH)
      gpio.output(self.allwheels[3],gpio.LOW)
  
  def turnleft(self):
      gpio.output(self.allwheels[0],gpio.HIGH)
      gpio.output(self.allwheels[1],gpio.LOW)
      gpio.output(self.allwheels[2],gpio.LOW)
      gpio.output(self.allwheels[3],gpio.HIGH)
 
  def changespeed(self,p,speed):
      p.ChangeDutyCycle(speed)
  
  def commend(self,s):
      if(s=="forward"):
        self.forward() 
      if(s=="backward"):
        self.backward()
      if(s=="stop"):
        self.stop()
      if(s=="left"):
        self.turnleft()
      if(s=="right"): 
        self.turnright()
      if(s=="up"):
        if(self.nowspeed<100):
          self.nowspeed+=10
          self.changespeed(self.p1,self.nowspeed)
          self.changespeed(self.p2,self.nowspeed)
      if(s=="down"):
        if(self.nowspeed>10):
          self.nowspeed-=10
          self.changespeed(self.p1,self.nowspeed)
          self.changespeed(self.p2,self.nowspeed)
if __name__ == "__main__":
    huang=auto([7,11,13,15,19,21])
    huang.commend("forward")
    input()
    huang.commend("stop")
