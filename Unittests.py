import unittest

from Books import Books
from BookStore import BookStore
from Customer import Customer
from Transaction import Transaction


class tester(unittest.TestCase):

  #TEsting
  def setUp(self):
    self.bookStoreManager = BookStore()
    self.customer = Customer('Bob')
    self.customer2 = Customer('Tina')
    self.book1 = Books('Hunger Games', 'authoer', 'ISBN', 'publisher', 2,
                       10.00)
    self.book2 = Books('Harry Potter', 'authoer2', 'ISBN2', 'publisher2', 1,
                       12.00)
    self.book3 = Books('The Book That doesnt Exist', 'authoer3', 'ISBN3', 'publisher2' , 1, 10.00)

    self.bookStoreManager.addBook(self.book1)
    self.bookStoreManager.addBook(self.book2)
    self.customer.addItem(self.book1)

  #Test Book class unittests
  def test_book_class(self):
    test_book = Books('title', 'author', 'ISBN', 'publisher', 1, 10.00)

    self.assertEqual(test_book.title, 'title')

#Test wishlist class unittests

  def test_wish_list_class(self):
    test_wishlist = Customer(2345)
    test_wishlist.addItem('book1')
    test_wishlist.addItem('book2')

    self.assertEqual(test_wishlist.wishList, ['book1', 'book2'])

  def test_wishlist_remove_item(self):
    test_wishlist = Customer(1234)
    test_wishlist.addItem('book1')
    test_wishlist.removeItem('book1')

    self.assertEqual(False, 'book1' in test_wishlist.wishList)

#test bookstore manager class unittests

  def test_print_transactions(self):
    testTransaction = Transaction(self.customer, self.book1, self.book1.price)
    self.bookStoreManager.purchase(self.customer, self.book1.title)
    temp = self.bookStoreManager.transactions[-1]
    self.assertEqual(testTransaction.transactionOwner.name, temp.transactionOwner)

  def test_book_store_remove_book_when_quantity_is_not_1(self):
    bookstore = BookStore()
    bookstore.addBook(self.book1)
    bookstore.removeBook(self.book1)
    temp = bookstore.findBook('Hunger Games')
    self.assertEqual(temp.quantity, 1)

  def test_book_store_remove_book_when_quantity_is_1(self):
    bookstore = BookStore()
    bookstore.addBook(self.book2)
    bookstore.removeBook(self.book2)
    temp = bookstore.findBook('Hunger Games')
    self.assertIsNone(temp)

  def test_bookstore_add_item(self):
    self.assertEqual(self.bookStoreManager.addBook(self.book1), self.book1)

  def test_bookstore_search(self):
    self.assertEqual(self.bookStoreManager.findBook('Hunger Games'),
                     self.book1)


#Integration Tests

  def test_bookstore_purchases_in_inventory_and_customer_wishlist(self):

    self.assertTrue(self.bookStoreManager.purchase(self.customer, self.book1.title))

  def test_bookstore_purchases_in_inventory_and_no_customer_wishlist(self):
    self.assertTrue(self.bookStoreManager.purchase(self.customer2, self.book2.title))
    
  def test_bookstore_purchases_not_in_inventory(self):
    self.assertFalse(self.bookStoreManager.purchase(self.customer2, self.book3.title))
    
if __name__ == '__main__':
  unittest.main()
