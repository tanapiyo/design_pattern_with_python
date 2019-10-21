from abc import ABCMeta, abstractmethod
import random
import time
import sys

#コスパ的に０−３と-のみ。
class BigChar():
  def __init__(self, charname:str):#コンストラクタで文字を作る
    self.charname = charname
    self.fontdata: str##と改行でできた書き込み対象
    readpath = "big" + self.charname + ".txt"
    with open(readpath, mode='r') as f:#ファイルは用意されている前提
      self.fontdata = f.read()

  def print(self) -> None:
  #def myprint(self) -> None:
    print(self.fontdata)
  
#BigCharインスタンスを生成する、シングルトン
from threading import Lock
class BigCharFactory():
  ####シングルトン用#####
  _unique_instance = None
  _lock = Lock() #クラスロック、マルチスレッド対応
  _pool = {}

  def __new__(cls):
    raise NotImplementedError('シングルトンだよ！')
  @classmethod
  def __internal_new__(cls) -> None:
    return super().__new__(cls)#こっちでnewを肩代わり
  @classmethod
  def get_instance(cls) -> 'BigCharFactory':
    if not cls._unique_instance:
      with cls._lock:
        if not cls._unique_instance:
          cls._unique_instance = cls.__internal_new__()#なければnewする
    return cls._unique_instance
  
  @classmethod
  def get_big_char(self, charname:str) -> 'BigChar':#マルチスレッドにしたい
    if not charname in BigCharFactory._pool:
      bigchar = BigChar(charname)
      BigCharFactory._pool[charname] = bigchar
    return BigCharFactory._pool[charname]

class BigString():
  def __init__(self, string:str) -> None:#1212123みたいなのがくる
    self.bigchars = {}
    self.factory = BigCharFactory.get_instance()
    for i, number in enumerate(list(string)):#1213とかが入っている
      self.bigchars[i] = self.factory.get_big_char(number)
  def print(self):
    for value in self.bigchars.values():
      value.print()
      

def main():
  if len(sys.argv) <= 1:
    print("Usage: python main.py 1212123")
    print("you can use number of 0-3")
    sys.exit()
  bigstring = BigString(sys.argv[1])
  bigstring.print()

if __name__ == "__main__":
    main()