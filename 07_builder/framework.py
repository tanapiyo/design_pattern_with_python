from abc import ABCMeta, abstractmethod

class Builder(metaclass=ABCMeta):
  @abstractmethod
  def make_title(self, title: str) -> None:
    pass
  
  @abstractmethod
  def make_string(self, string: str) -> None:
    pass

  @abstractmethod
  def make_items(self, items: list) -> None:
    pass
  
  @abstractmethod
  def close(self) -> None:
    pass

#Builderを使って文書を作る
class Director():
  def __init__(self, builder: Builder):
    self.builder = builder

  def construct(self) -> None:
    self.builder.make_title("Greeting")
    self.builder.make_string("朝から昼にかけて")
    self.builder.make_items(["おはようございます。", "こんにちは。"])
    self.builder.make_string("夜に")
    self.builder.make_items(["こんばんは。", "おやすみなさい。", "さようなら。"])
    self.builder.close()
  