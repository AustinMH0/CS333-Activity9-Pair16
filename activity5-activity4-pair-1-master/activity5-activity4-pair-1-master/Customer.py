class Customer:

  def __init__(self, name):
    self.name = name
    self.wishList = []
    return None

  def addItem(self, item):
    self.wishList.append(item)

  def removeItem(self, item):
    self.wishList.remove(item)
