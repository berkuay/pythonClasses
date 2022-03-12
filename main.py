class Item:
    pay_Rate = 0.8  # The pay rate after discount
    all = []  # itemler için oluşturulan boş liste

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"price is under zero: {price}"
        assert quantity >= 0, f"quantity is under zero: {quantity}"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)  # all listesine Item clasındaki her instanceı eklemek için oluşturuldu

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_Rate
        # Item.pay_Rate -> sadece class leveldeki değeri alır. Eğer self.pay_Rate kullanılırsa
        # spesifik olarak atanan değeri alır, herhangi bir değer belirtilmezse class levelda olan
        # rate kullanılır.

    def __repr__(self): # objeleri consola yazdırdığında kontrol edebilmek için
        return f"Item('{self.name}','{self.price}','{self.quantity}')"


# item1 = Item("phone", 100, 2)
# item1.apply_discount()
# print(item1.price)

# print(Item.__dict__)
# print(item1.__dict__)

# item2 = Item("laptop", 1000, 5)
# item2.pay_Rate = 0.7
# item2.apply_discount()
# print(item2.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

