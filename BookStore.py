from Transaction import Transaction


class BookStore:

  def __init__(self):
    self.inventory = []
    self.transactions = []

  def addBook(self, book):
    self.inventory.append(book)
    return self.inventory[-1]

  def removeBook(self, book):
    if book.quantity == 1:
      book.quantity = 0
      self.inventory.remove(book)
    else:
      book.quantity -= 1

  def findBook(self, bookTitle):
    for book in self.inventory:
      if book.title == bookTitle:
        return book

    return None

  def wishlistPurchase(self, wishlist):
    bookRemoved = False
    for book in wishlist.wishList:
      temp = self.findBook(book)
      if temp is not None and temp.quantity != 0:
        wishlist.removeItem(book)
        self.removeBook(book)
        bookRemoved = True

    return bookRemoved

  def purchase(self, customer, item):
    bookRemoved = False
    if len(customer.wishList) != 0:
      for book in customer.wishList:
        temp = self.findBook(book.title)
        if temp is not None and temp.quantity != 0:
          self.transactions.append(Transaction(customer.name, temp,
                                               temp.price))
          customer.removeItem(temp)
          self.removeBook(temp)
          bookRemoved = True
    elif item is not None:
      temp = self.findBook(item)
      print(temp)
      if temp is not None and temp.quantity != 0:
        self.transactions.append(Transaction(customer.name, temp, temp.price))
        self.removeBook(temp)
        bookRemoved = True

    return bookRemoved
