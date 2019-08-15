#printはI/F
#抽象クラスにしたいので
from abc import ABCMeta, abstractmethod

class Print(metaclass=ABCMeta):
  @abstractmethod
  def print_weak(self):
    pass

  @abstractmethod
  def print_strong(self):
    pass