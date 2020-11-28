# def dollarize(num):    
#     print(f"$ {num:,.2f}")
#     return num


# class MoneyFmt:
#     amount = 0

#     def __init__(self, amount):
#         self.amount = amount
       
#     @classmethod
#     def update(cls,amount):
#         return cls.amount 

#     def __repr__(self):
#         return float(self.amount)

#     def str(self):
#         return dollarize(self.amount)
    


# obj = MoneyFmt(float(input("Enter num:")))
# obj.str()
# obj.update(5000)
# print(obj.amount)


##2

# class Bike:
#     def __init__(self,cost,make,model,year,condition,_sale_price =None,sold = False):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = None
#         self.sold = False

#     def income(self,_sale_price,profit): 
#         self.profit = profit  
#         self._sale_price = _sale_price     
#         if self._sale_price <= self.cost:
#             self._sale_price = self.cost + self.profit
#             print(f'Sale price is {self._sale_price}')
#             return _sale_price
#         print(f"Sale price {self._sale_price}")
#         return self._sale_price

#     def service(self,service_cost,condition):
#         self.service_cost = service_cost
#         self.condition = condition
#         self._sale_price = self.cost + self.profit + self.service_cost 
#         print(f"Service cost was {self.service_cost}, condition {self.condition}")
#         return self._sale_price
    
#     def sell(self):
#         return self.sold == True

#     def get_default_bike(self):
#         self.income(int(input("Enter sale price: ")),int(input("Enter your margin: ")))
#         self.service(int(input("Enter service cost: ")),input("Enter condition:"))
#         self.sell()
#         print(f"Bike {self.make} {self.model} designed in {self.year}, was bought by {self.cost}.")

# bike = Bike(2000,"Kama","450i",2018,"used")
# bike.get_default_bike()

##3

