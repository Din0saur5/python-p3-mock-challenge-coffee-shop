
from statistics import mean
class Coffee:
    def __init__(self, name):
        self.name = name
    
    def set_name(self, name):
        x = hasattr(self, 'name')
        if x: 
            print('coffee already has a name')
        else:
            if type(name) == str and len(name) > 3:
                self._name = name
            else:
                print("name must be a str and greater than 3 char ")
        
    def get_name(self):
        return self._name
     
    name = property(get_name, set_name)
    
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        
        return list({order.customer for order in Order.all if order.coffee is self})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if len(self.orders()) > 0:
            return mean([order.price for order in self.orders()])
class Customer:
    def __init__(self, name):
        self.name = name
     
    def set_name(self, name):
        if type(name) == str and len(name) in range(1,16):
            self._name = name
        else:
            print("name must be a str contatining 1-15 char")
        
    def get_name(self):
        return self._name
    name = property(get_name, set_name)
    
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in Order.all if order.customer is self})
    
    def create_order(self, coffee, price):
        order = Order(self, coffee,price)
        return order
    
class Order:
    all=[]
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self) 
        
    def set_price(self, price):
        if isinstance(price, float) and price > 1.0 and price <10.0 and not hasattr(self, 'price'):
           self._price = price
        
    def get_price(self):
        return self._price
     
    price = property(get_price, set_price)    
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

# coffee = Coffee("Vanilla Latte")
# customer = Customer("Steve")
# customer_2 = Customer("Dima")
# order1 = Order(customer, coffee, 2.0)
# order2 = Order(customer_2, coffee, 2.0)
# order3 = Order(customer, coffee, 5.0)
