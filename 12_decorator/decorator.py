from abc import ABCMeta, abstractmethod
import traceback


class Display(metaclass=ABCMeta):
    @abstractmethod
    def get_columns(self) -> int:
        pass
    @abstractmethod
    def get_rows(self) -> int:
        pass
    @abstractmethod
    def get_row_text(self, row: int) -> str:
        pass
    def show(self) -> None:
      for i in range(self.get_rows()):
        print(self.get_row_text(i))

'''
一行の文字列を表示するクラス
'''
class StringDisplay(Display):
  def __init__(self, string: str):
    self.__string = string

  def get_columns(self) -> int:
    return len(self.__string)
  
  def get_rows(self) -> int:
    return 1
  
  def get_row_text(self, row: int) -> str:
    if (row == 0):
      return self.__string
    else:
      return None

'''
飾り枠を表すクラス（中身と同じIF）
'''
class Border(Display):
  def __init__(self, display: 'Display'):
    self.display = display


'''
左右に決まった文字で飾り付けるクラス
'''
class SideBorder(Border):
  def __init__(self, display: 'Display', char: str):
    super().__init__(display)
    self.__border_char = char

  def get_columns(self) -> int:
    return 1 + self.display.get_columns() + 1
  
  def get_rows(self) -> int:
    return self.display.get_rows()
  
  def get_row_text(self, row: int) -> str:
    return self.__border_char + self.display.get_row_text(row) + self.__border_char

'''
上下左右に決まった文字で飾り付けるクラス
'''
class FullBorder(Border):
  def __init__(self, display: 'Display'):
    super().__init__(display)

  def get_columns(self) -> int:
    return 1 + self.display.get_columns() + 1
  
  def get_rows(self) -> int:
    return 1 + self.display.get_rows() + 1
  
  def get_row_text(self, row: int) -> str:
    if(row == 0):#上の枠線
      return "+" + self.__make_line('-', self.display.get_columns()) + "+"
    elif(row == self.display.get_rows()+1):#下の枠線
      return "+" + self.__make_line('-', self.display.get_columns()) + "+"
    else:
      return "|" + self.display.get_row_text(row-1) + "|"

  def __make_line(self, char: str, count: int):
    __buf:list = []
    for i in range(count):
      __buf.append(char)
    return (' '.join(__buf))


def main():
    b1 = StringDisplay("Hello, world.")#"b1: Hello, world."を飾りなしで表示する
    b2 = SideBorder(b1, "#")#b1に対して左右に#をつける
    b3 = FullBorder(b2)#b2に対して全体の飾り枠をつける
    b1.show()
    b2.show()
    b3.show()
    b4 = SideBorder(
            FullBorder(
              FullBorder(
                SideBorder(
                  FullBorder(
                    StringDisplay("こんにちは。")
                  )
                ,'*'), 
              )
            )
      ,"/")
    b4.show()


if __name__ == "__main__":
    main()
