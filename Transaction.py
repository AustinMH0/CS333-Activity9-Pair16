from datetime import datetime

class Transaction:
  def __init__(self, customername, books,price):
    self.transactionOwner= customername
    self.transactionTime = datetime.now()
    self.books= []
    self.transactionPrice = price
    if books is not None:
      self.books.append(books)

    
  # def getName(self, customerName,Bookstore) :
  #   for customer in Bookstore.customers:
  #     if customer.name == customerName:
  #       return customer
    
  
  # def getBooknames(self):
  #   return None

  # def getPrice(self):
  #   return None

  # def recordTransaction(self, customer, item):
  #   self.bookstore.transactions.append()
  #   return None

