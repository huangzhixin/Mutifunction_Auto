from network import UnmannedNet
from control import Auto
from eye import Eye
import time 
brain = UnmannedNet(768,60,2)
auto = Auto([29,31,33,35,38,40])
eye=Eye("192.168.10.1")
brain.loadnetwork()
while(1):
  inputdata = self.eye.getResizeImage()
  control=self.brain.prediction(inputdata)
  beta=control[0]  
  gamma=control[1]
  auto.control(beta,gamma)
  time.sleep(0.1)
