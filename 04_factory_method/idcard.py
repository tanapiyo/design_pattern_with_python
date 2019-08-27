from framework import Product, Factory

class IdCard(Product):
  def __init__(self, owner):
    self.__owner = owner
    print(self.__owner + "のカードを作ります。")
  
  def use(self):
    print(self.__owner + "のカードを使います。")
  
  def get_owner(self):
    return self.__owner

class IdCardFactory(Factory):
  def __init__(self):
    self.__owners = []

  def _create_product(self, owner):
    return IdCard(owner)
  
  def _register_product(self, product):
    self.__owners.append(product.get_owner())
  
  def get_owners(self):
    return self.__owners