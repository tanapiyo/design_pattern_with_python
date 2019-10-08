from abc import ABCMeta, abstractmethod

class Trouble():
  def __init__(self, number: int):
    self.number = number
  
  def __str__(self):
    return "[Trouble" + str(self.number) + "]"

class Support(metaclass=ABCMeta):#ここに処理の流れを実装
  def __init__(self, name: str):
    self.name = name
    self.next = None
  
  def set_next(self, next: 'Support') -> 'Support':
    self.next = next
    return self.next
  
  def support(self, trouble: 'Trouble') -> None:
    if(self.resolve(trouble)):
      self.done(trouble)
    elif(self.next is not None):
      self.next.support(trouble)#たらいまわし
    else:
      self.fail(trouble)

  @abstractmethod
  def resolve(self, trouble: 'Trouble') -> bool:
    pass
  
  def done(self, trouble: 'Trouble') -> None:
    print(str(trouble) + "is resolved by" + str(self) + ".")
  
  def fail(self, trouble: 'Trouble') -> None:
    print(str(trouble) + "cannot be resolved.")

class NoSupport(Support):#resolveで何もしてくれないクラス
  def __init__(self, name: str):
    super().__init__(name)
  
  def resolve(self, trouble: 'Trouble') -> bool:
    return False#何もしない
  
class LimitSupport(Support):#limitで指定した番号未満を解決するクラス
  def __init__(self, name: str, limit: int):
    super().__init__(name)
    self.__limit = limit
  
  def resolve(self, trouble: 'Trouble') -> bool:
    if(trouble.number < self.__limit):
      return True
    else:
      return False

class OddSupport(Support):#奇数番号のトラブルを解決するクラス
  def __init__(self, name: str):
    super().__init__(name)
  
  def resolve(self, trouble: 'Trouble') -> bool:
    if(trouble.number % 2 == 1):
      return True
    else:
      return False

class SpecialSupport(Support):#指定した番号のトラブルだけ解決するクラス
  def __init__(self, name: str, number: int):
    super().__init__(name)
    self.__number = number
  
  def resolve(self, trouble: 'Trouble') -> bool:
    if(trouble.number == self.__number):
      return True
    else:
      return False
  
def main():
  alice = NoSupport("Alice")
  bob = LimitSupport("Bob", 100)
  charlie = SpecialSupport("Charlie", 429)
  diana = LimitSupport("Diana", 200)
  elmo = OddSupport("Elmo")
  fred = LimitSupport("Fred", 300)
  #連鎖をつくる。連結リストみたい…
  alice.set_next(bob).set_next(charlie).set_next(diana).set_next(elmo).set_next(fred)
  #トラブルを発生させる
  for i in range(0, 500, 33):
    alice.support(Trouble(i))


if __name__ == "__main__":
    main()