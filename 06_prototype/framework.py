from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
  @abstractmethod
  def use(self, string):
    pass
  
  @abstractmethod
  def create_clone(self):
    pass

class Manager():
  def __init__(self):
    self.showcase = {}

  def register(self, name, proto):
    self.showcase[name] = proto
  
  def create(self, protoname):
    __p = self.showcase[protoname]
    return __p.create_clone()