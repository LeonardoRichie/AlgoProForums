from ShoppinglistLR import Shoppinglist


def createList(counts):
    li = []
    while counts <= 0:  # inputing count above 0
        princounts = int(input("How many items will you order today? "))
        b1 = Shoppinglist("t", 0, 0, 0)
    for k in range(1, counts + 1):  # inputing names & amount
        print("item #{}".format(k))
        name = str(input("Enter food: "))
        amount = float(input("Enter Amount of pounds: "))
        while amount <= 0:  # inputing amount above 0
            print("Amount of pounds must be greater than 0.")
            amount = float(input("Enter Amount of pounds: "))
        price = 0
        priceord = 0
        li.append(Shoppinglist(name, amount, price, priceord))  # putting into a list
        print()
    return(li)


def printList(list):
    print("Here's a summary of the items purchased:")
    print("-------------------------------")
    for k in list:  # printing the list (Item, Amount Ordered, Price per pound & Price of order)
        print(k)
        print()

def calculateTotal(counts, list):
    z = 0
    for k in range(0, counts):  # calculate the total cost of all the items in the list
        x = (list[k])
        y = x.getPriceOrderedLR()
        z = z + y

    print("Total cost: {:.2f}".format(z))

def main():
    counts = int(input("How many items will you order today? "))
    x = createList(counts)
    y = printList(x)
    z = calculateTotal(counts, x)


main() #Run the function

"""
Here is the main function to input the name and amount. It also prints the
list using for loop.
"""