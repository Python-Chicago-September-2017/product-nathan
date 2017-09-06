class Product(object):
    def __init__(self,price,item_name,weight,brand,cost):
        self.price = float(price)
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For sale"
    def sell(self):
        self.status = "Sold"
        return self
    def tax(self,tax):
        self.price *= (tax + 1)
        return self
    def return_product(self,reason):
        if reason.lower() == "defective":
            self.status = "Defective"
            self.price = 0
        elif reason.lower() == "closed":
            self.status = "For sale"
        elif reason.lower() == "opened":
            self.status = "Opened"
            self.price *= 0.80
        return self
    def display_info(self):
        print "Price: " + str(self.price)
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
        print "Status: " + str(self.status)

product_1 = Product(3,"Chips","0.3lbs","Lays",0.5)

print "#1"
product_1.display_info()
print "2#"
product_1.tax(0.06).display_info()
print "3#"
product_1.sell().display_info()
print "4#"
product_1.return_product("Defective").display_info()
