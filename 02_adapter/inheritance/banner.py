#Bannerはあらかじめ提供されている
class Banner():
  def __init__(self, string):
    self.__string = string
  
  def show_with_paren(self):
    print('({})'.format(self.__string))
  
  def show_with_aster(self):
    print('*{}*'.format(self.__string))