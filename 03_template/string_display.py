from abstract_display import AbstractDisplay

class StringDisplay(AbstractDisplay):
  def __init__(self, string):
    self.__string = string
    self.__width = len(string)

  def open(self):
    self.__print_line()
  
  def print(self):
    print(self.__string)
  
  def close(self):
    self.__print_line()
  
  def __print_line(self):
    print("+", end='')
    for i in range(self.__width):
      print("-", end='')
    print("+")


  
