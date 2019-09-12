from abc import ABCMeta, abstractmethod
class DisplayImpl(metaclass=ABCMeta):
  @abstractmethod
  def raw_open(self) -> None:
    pass
  @abstractmethod
  def raw_print(self) -> None:
    pass
  @abstractmethod
  def raw_close(self) -> None:
    pass

class StringDisplayImpl(DisplayImpl):
  def __init__(self, string: str):
    self.__string = string
    self.__width = len(string)

  def raw_open(self) -> None:
    self.__print_line()

  def raw_print(self) -> None:
    print("|%s|" % self.__string)

  def raw_close(self) -> None:
    self.__print_line()

  def __print_line(self) -> None:
    print("+", end="")
    for i in range(self.__width):
      print("-", end="")
    print("+")
    
#Displayは基本の機能の実装とIF
class Display(metaclass=ABCMeta):
  def __init__(self, impl: DisplayImpl):
    self.__impl = impl

  #@abstractmethod
  def open(self) -> None:#open, print, closeはpublicなの？子からよぶからか
    self.__impl.raw_open()
  
  #@abstractmethod
  def print(self) -> None:
    self.__impl.raw_print()
  
  #@abstractmethod
  def close(self) -> None:
    self.__impl.raw_close()
  
  #@abstractmethod
  def display(self) -> None:
    self.open()
    self.print()
    self.close()

#CountDisplayで機能の追加
class CountDisplay(Display):
  def __init__(self, impl: DisplayImpl):
    super().__init__(impl)
  
  def multi_display(self, times: int) -> None:
    super().open()
    for _ in range(times):
      super().print()
    super().close()

