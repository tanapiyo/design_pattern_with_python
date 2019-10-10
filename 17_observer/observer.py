from abc import ABCMeta, abstractmethod
import random
import time

class Observer(metaclass=ABCMeta):
  @abstractmethod
  def update(self, generator: 'NumberGenerator')->None:
    pass

class NumberGenerator(metaclass=ABCMeta):
  def __init__(self):
    self.observers = []
  
  def add_observer(self, observer: 'Observer') -> None:
    self.observers.append(observer)
  
  def delete_observer(self, observer: 'Observer') -> None:
    self.observers.remove(observer)
  
  def notify_observers(self) -> None:
    for observer in self.observers:
      observer.update(self)

  @abstractmethod
  def get_number(self) -> int:
    pass

  @abstractmethod
  def execute(self) -> int:
    pass
  

class RandomNumberGenerator(NumberGenerator):
  def __init__(self):
    super().__init__()
    self.__number = 0
  
  def get_number(self) -> int:
    return self.__number
  
  def execute(self)->None:
    self.__number = random.randint(0,50)
    self.notify_observers()

class DigitObserver(Observer):
  def update(self, generator: 'NumberGenerator') -> None:
    print("DigitObserver:" + str(generator.get_number()))
    try:
      time.sleep(0.1)
    except:
      pass

class GraphObserver(Observer):
  def update(self, generator: 'NumberGenerator') -> None:
    print("GraphObserver:")
    __count = generator.get_number()
    for _i in range(__count):
      print("*", end="")
    try:
      time.sleep(0.1)
    except:
      pass

def main():
  generator = RandomNumberGenerator()
  observer1 = DigitObserver()
  observer2 = GraphObserver()
  generator.add_observer(observer1)
  generator.add_observer(observer2)
  generator.execute()

if __name__ == "__main__":
    main()