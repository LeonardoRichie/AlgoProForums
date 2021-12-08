class Shoppinglist:
    def __init__(self, name, amount, price, priceord):
        # initializer method
        self.__Name = str(name)
        self.__Amount = float(amount)
        self.__Price = price
        self.__PriceOrdered = priceord
        self.__pricelistLR()
        self.countcostLR()

    # list of pricelist
    def __pricelistLR(self):
        if self.__Name:
            if self.__Name == "Dry Cured Iberian Ham":
                self.__Price = 177.80
            elif self.__Name == "Wagyu Steaks":
                self.__Price = 450.00
            elif self.__Name == "Matsutake Mushrooms":
                self.__Price = 272.00
            elif self.__Name == "Kopi Luwak Coffee":
                self.__Price = 306.50
            elif self.__Name == "Moose Cheese":
                self.__Price = 487.20
            elif self.__Name == "White Truffles":
                self.__Price = 3600.00
            elif self.__Name == "Blue Fin Tuna":
                self.__Price = 3603.00
            elif self.__Name == "Le Bonnotte Potatoes":
                self.__Price = 270.81
        else:
            self.__Price = 0.00

    #Return a value
    def getNameLR(self):
        return self.__Name
    def getAmountLR(self):
        return self.__Amount
    def getPriceLR(self):
        return self.__Price
    def getPriceOrderedLR(self):
        return self.__PriceOrdered

    # Calculate Total cost
    def countcostLR(self):
        self.__PriceOrdered = self.__Amount * self.__Price

    #Accessors(To print the list)
    def __str__(self):
        return "Item: {}\nAmount ordered: {} pounds\nPrice per pound: ${:.2f}\nPrice of order: ${:.2f}"\
            .format(self.getNameLR(), self.getAmountLR(), self.getPriceLR(), self.getPriceOrderedLR())

"""
Here is my class module which is used to store the pricelist of the food, store
the food name, price, amount, and total price. the __str__ is used to print the
shopping list format and the countcost is used to count the total number of
ordered foods.
"""