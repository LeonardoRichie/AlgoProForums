from ShoppinglistLR import Shoppinglist


def createList():
    li = []
    counts = int(input("How many items will you order today? "))
    while counts <= 0:  # inputing count above 0
        print("Number of items must be at least 1.")
        counts = int(input("How many items will you order today? "))
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
    listing = [counts]
    listing.append(li)
    return(listing)


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

    print("Total cost: ${:.2f}".format(z))

def main():#main function
    x = createList()
    y = printList(x[1])
    z = calculateTotal(x[0], x[1])


main() #Run the function

"""
Here is the main function to input the name and amount. It also prints the
list using for loop.
"""