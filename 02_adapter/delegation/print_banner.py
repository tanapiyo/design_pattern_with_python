#adapter
#printerもbannerももつ

#BANNERインスタンスをもってそこにわたすか
#親クラスのメソッドを使うのかの違い
#親とかインスタンス作るとかが使いたいレガシーコードとかになる

#?printいらなくない？

from print import Print# 追加
from banner import Banner

#class PrintBanner(Banner):
class PrintBanner(Print):

  def __init__(self, string):
    #super().__init__(string)
    self.__banner = Banner(string)
  
  def print_weak(self):
    self.__banner.show_with_paren()

  def print_strong(self):
    self.__banner.show_with_aster()