from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
  @abstractmethod
  def use(self):
    pass

    
class Factory(metaclass=ABCMeta):
  @abstractmethod
  def _create_product(self, owner):
    pass
  
  @abstractmethod
  def _register_product(self, product):
    pass

  def create(self, owner):
    #self.__p = self._create_product(owner)
    #self._register_product(self.__p)
    #return self.__p
    __p = self._create_product(owner)#ローカル変数でいい
    self._register_product(__p)
    return __p
    