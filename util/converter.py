from abc import ABC, abstractmethod
from users import Cashier, Customer
from products import Product

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self, dataFrame) -> list:    
    cashiers = []
    for _, row in dataFrame.iterrows():
      c = Cashier(str(row['dni']), str(row['name']), int(row['age']), str(row['timetable']), float(row['salary']))
      cashiers.append(c)
    return cashiers

class CustomerConverter(Converter):
  def convert(self, dataFrame) -> list:
    customers = []
    for _, row in dataFrame.iterrows():
      c = Customer(str(row['dni']), str(row['name']), int(row['age']), str(row['email']), str(row['postalcode']))
      customers.append(c)
    return customers

class ProductConverter(Converter):
  def convert(self, dataFrame, product_class) -> list:
    products = []
    for _, row in dataFrame.iterrows():
      p = product_class(str(row['id']), str(row['name']), float(row['price']))
      products.append(p)
    return products