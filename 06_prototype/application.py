from framework import Product, Manager
import copy

class MessageBox(Product):
  def __init__(self, decochar: str):
    self.decochar = decochar
  
  def use(self, string: str) -> None:
    __length = len(string)#いる？
    for i in range(__length + 4):
      print(self.decochar, end='')
    print("")
    print(self.decochar + " " + string + " " + self.decochar)
    for i in range(__length + 4):
      print(self.decochar, end='')
    print("")
  
  def create_clone(self) -> Product:
    return copy.deepcopy(self)#自分をコピーしてかえしてあげる

class UnderlinePen(Product):
  def __init__(self, ulchar: str):
    self.ulchar = ulchar
  
  def use(self, string) -> None:
    length = len(string)
    print('"' + string + '"')
    #print(" ")
    for i in range(length):
      print(self.ulchar, end="")
    print("")

  def create_clone(self) -> Product:
    return copy.deepcopy(self)