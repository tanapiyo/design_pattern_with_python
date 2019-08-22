from abstract_display import AbstractDisplay

class CharDisplay(AbstractDisplay):
  def __init__(self, ch):
    self.__ch = ch

  def open(self):
    print("<<", end='')
  
  def print(self):
    print(self.__ch, end='')
  
  def close(self):
    print(">>")
  
