from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from numpy import ndarray
class UnmannedNet:
  def __init__(self,n_in,n_hidden,n_out):
      self.net = FeedForwardNetwork()
      inLayer = LinearLayer(n_in)
      hiddenLayer1 = SigmoidLayer(n_hidden) 
      hiddenLayer2 = SigmoidLayer(n_hidden) 
      outLayer = LinearLayer(n_out)
      self.net.addInputModule(inLayer)
      self.net.addModule(hiddenLayer1)
      self.net.addModule(hiddenLayer2)
      self.net.addOutputModule(outLayer)
      in_to_hidden = FullConnection(inLayer, hiddenLayer1)
      hidden_to_out = FullConnection(hiddenLayer2, outLayer)
      hidden_to_hidden = FullConnection(hiddenLayer1, hiddenLayer2)
      self.net.addConnection(in_to_hidden)
      self.net.addConnection(hidden_to_hidden)
      self.net.addConnection(hidden_to_out)
      self.net.sortModules()
      #self.net.params
      self.ds = SupervisedDataSet(n_in, n_out)

  def load_network(self,fName='./data/mynetwork.xml'):
      self.net = NetworkReader.readFrom(fName)

  def save_network(self,fName='./data/mynetwork.xml'):
      NetworkWriter.writeToFile(self.net, fName)

  def train(self,number):
      self.trainer = BackpropTrainer(self.net, self.ds)
      self.trainer.trainEpochs(number)
  
  def add_data(self,image,control):
      self.ds.addSample(image, control)

  def save_data(self,fName="./data/mydata"):
      SupervisedDataSet.saveToFile(self.ds, fName)

  def read_data(self,fName="./data/mydata"):
      self.ds = SupervisedDataSet.loadFromFile(fName)

  def prediction(self,image):
      return self.net.activate(image)

  def evaluate(self,valueFaultTolerant):
      target = self.ds.data.get('target')
      inputvalue = self.ds.data.get('input')
      numberOfSample = target.shape[0]
      numberOfCorrect = 0
      for i in range(0,numberOfSample):
         if (abs(target[i]-self.prediction(inputvalue[i]))<=valueFaultTolerant):
            numberOfCorrect+=1
      print "Correct rate is"+str(float(numberOfCorrect)/float(numberOfSample)) 
      
if __name__ == "__main__":
   huang = UnmannedNet(768,60,2)
   huang.read_data()
   print "start training"
   huang.train(3)
   print "start evaluate"
   huang.evaluate(5)
   huang.evaluate(2)
   huang.save_network()
   """
   huang = UnmannedNet(2,5,1)
   for i in range(-50,50):
    for j in range (-50,50):
      if(i<=j):
        huang.add_data((i, j), (0))
      else:
        huang.add_data((i, j), (1))
   #huang.save_data()
   #huang.read_data()
   print "start training"
   huang.train(5)
   print "start evaluate"
   huang.evaluate(0.2)
   for i in range(-50,50):
    for j in range (-50,50):
      print str(i)+" "+str(j)+"   "+str(huang.output([i,j]))
   """
