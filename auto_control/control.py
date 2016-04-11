# -*- coding:utf-8 -*-  
import RPi.GPIO as gpio
import time
class Auto:
  def __init__(self,wheels):
    gpio.setmode(gpio.BOARD)     
    self.allwheels=wheels
    self.rightwheel=wheels[0:2]
    self.leftwheel=wheels[2:4]
    self.pwm=wheels[4:6]
    print self.rightwheel ,self.leftwheel, self.pwm
    gpio.setmode(gpio.BOARD)
    for port in wheels:
      gpio.setup(port,gpio.OUT)
    self.p1=gpio.PWM(self.pwm[0], 60)
    self.p2=gpio.PWM(self.pwm[1], 60)
    self.nowspeed1=0
    self.nowspeed2=0
    self.p1.start(self.nowspeed1)
    self.p2.start(self.nowspeed2)
   
  def control(self,beta,gamma):
     if -30<=beta<=15 :
        if -40<=gamma<=40 :
           self.forward()
           self.turn(beta,gamma)
        if -50<=gamma<-40 :
           self.turnleft()
           self.turn(beta,gamma)
        if 40<gamma<=50 :
           self.turnright()
           self.turn(beta,gamma)
     if 15<beta<25 :
        if gamma<-40 :
           self.changespeed(self.p1,100)
           self.changespeed(self.p2,100)
           self.turnleft()
           print "left!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        if 40<gamma :
           self.changespeed(self.p1,100)
           self.changespeed(self.p2,100)
           self.turnright()
           print "right!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        if -40<gamma<=40 :
           self.nowspeed1=0
           self.nowspeed1=0
           self.stop()
     if 25<=beta<=60 :
        if -50<=gamma<=50 :
           self.backward()
           self.turn(beta,gamma)
        if -50<=gamma<-40 :
           self.turnright()
           self.turn(beta,gamma)
        if 40<gamma<=50 :
           self.turnleft()
           self.turn(beta,gamma)
 
  def turn(self,beta,gamma):
      self.nowspeed1=int(float(100/50)*abs((15-beta))+20)
      self.nowspeed2=int(float(100/50)*abs((15-beta))+20)
      self.nowspeed1=int(abs(self.nowspeed1*(float(1+gamma/30))))
      self.newspeed2=int(abs(self.nowspeed2*(float(1-gamma/30))))
      if(self.nowspeed1>100):
          self.nowspeed1=100
      if(self.nowspeed2>100):
          self.nowspeed2=100 
      self.changespeed(self.p1,self.nowspeed1)
      self.changespeed(self.p2,self.nowspeed2)
      print self.nowspeed1, self.nowspeed2
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
  
  def turnleft(self):
      gpio.output(self.allwheels[0],gpio.LOW)
      gpio.output(self.allwheels[1],gpio.HIGH)
      gpio.output(self.allwheels[2],gpio.HIGH)
      gpio.output(self.allwheels[3],gpio.LOW)
  
  def turnright(self):
      gpio.output(self.allwheels[0],gpio.HIGH)
      gpio.output(self.allwheels[1],gpio.LOW)
      gpio.output(self.allwheels[2],gpio.LOW)
      gpio.output(self.allwheels[3],gpio.HIGH)
 
  def changespeed(self,p,speed):
      p.ChangeDutyCycle(speed)
  
if __name__ == "__main__":
    huang=Auto([29,31,33,35,38,40])
    huang.control(20,0)
    time.sleep(3)
    huang.control(0,-35)
    time.sleep(5)
    huang.control(0,35)
    time.sleep(5)
    huang.control(40,0)
    time.sleep(3)
    huang.control(20,0)
