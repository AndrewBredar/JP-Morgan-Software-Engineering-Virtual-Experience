import unittest
from client3 import getRatio, getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 115.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    # I combined the first and second tests to make it more concise.
    # Also, in the fourth quote above, the original top_ask price was higher than the top_bid price.
    # I changed it to be lower than the top_bid price in order to have two quotes where the top_bid price
    # is lower than the top_ask price (as the guide intended, I believe).

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  #Assert that getRatio returns None when price_b equals zero
  def test_getRatio_priceBZero(self):
    price_a = 100.50
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))
  
  #Assert that getRatio returns zero if price_a is zero
  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 100.50
    self.assertEqual(getRatio(price_a, price_b), 0)

  #If price_a is greater than price_b the ratio should be > 1
  def test_getRatio_greaterThan1(self):
    price_a = 200.50
    price_b = 100.50
    self.assertGreater(getRatio(price_a, price_b), 1)

  #If price_a is less than price_b the ratio should be < 1
  def test_getRatio_lessThan1(self):
    price_a = 50.50
    price_b = 100.50
    self.assertLess(getRatio(price_a, price_b), 1)

  #If price_a is equal to price_b the ratio should be 1
  def test_getRatio_exactlyOne(self):
    price_a = 100.50
    price_b = 100.50
    self.assertEqual(getRatio(price_a, price_b), 1)

if __name__ == '__main__':
    unittest.main()
