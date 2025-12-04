class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    
    def price_order(self, item):
        return DeliveryOrder(item.price)

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def delivery(self, name, order):
        print(f"{self.name} is delivering {order} to {name} using {self.vehicle}")

class DeliveryOrder:
    def __init__(self, customer, item, status):
        self.customer = customer
        self.item = item
        self.status = status
    
    def assign_driver(self, driver):
        return f"""Order Summary:
Item: {self.item}
Status: {self.status}
Driver: {driver}"""

    def summary(self):
        return f"""Order for {self.item} → delivered"""

c1 = Person("Alice")
c2 = Person("Bob")
c3 = Person("David")

c1.introduce()
c2.introduce()
c3.introduce()
print()

c1 = Customer("Alice", "Newyork")
c2 = Customer("Bob", "Newyork")
c3 = Driver("David", "motorcycle")

d1 = DeliveryOrder(c1, "Laptop", "preparing")
d2 = DeliveryOrder(c2, "Headphones", "preparing")

print(d1.assign_driver(c3.name))
print()
print(d2.assign_driver(c3.name))
print()

c3.delivery(c1.name, d1.item)
c3.delivery(c2.name, d2.item)

print()
print("Final Status:")
print(d1.summary())
print(d2.summary())