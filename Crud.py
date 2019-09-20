from tkinter import *

class Item:
    def __init__(self, NAME, PRICE, QUANTITY):
        self.name = NAME
        self.price = PRICE
        self.quantity = QUANTITY

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def updateSelf(self, NAME, PRICE, QUANTITY):
        self.name = NAME
        self.price = PRICE
        self.quantity = QUANTITY
        viewItems()


def addItem():
    global items
    item = Item(i1.get(), i2.get(), i3.get())
    items.append(item)
    viewItems()

def deleteItem(item):
    global items
    items.remove(item)
    viewItems()

def updateItem(item):
    i1.insert(0,item.getName())
    i2.insert(0,item.getPrice())
    i3.insert(0,item.getQuantity())
       

def viewItems():
    global items
    
    row = 1
    list = organizer.grid_slaves()
    for l in list:
        l.destroy()
        
    addHeaders()
    for item in items:
        Label(organizer, text=item.getName(), width=10).grid(row=row, column=0, sticky=S , padx=10, pady=5)
        Label(organizer, text=item.getPrice(), width=10).grid(row=row, column=1, sticky=S , padx=10, pady=5)
        Label(organizer, text=item.getQuantity(), width=10).grid(row=row, column=2, sticky=S , padx=10, pady=5)

        bt1 = Button(organizer, text="UPDATE", width=7, command=lambda prod=item: updateItem(prod))
        bt1.grid(row=row, column=3, sticky=W, padx=5, pady=5)
        
        bt2 = Button(organizer, text="DELETE", width=7, command=lambda prod=item: deleteItem(prod))
        bt2.grid(row=row, column=4, sticky=E, padx=5, pady=5)
        row += 1


def addHeaders():    
    organizer.grid(row=5, column=0, columnspan=5, pady=5, sticky=S)
    Label(organizer, text="Name", width=10).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(organizer, text="Price", width=10).grid(row=0, column=1, sticky=W, padx=10, pady=5)
    Label(organizer, text="Quantity", width=10).grid(row=0, column=2, sticky=W, padx=10, pady=5)

items = []

root = Tk()
root.title("-------------------INVENTORY SYSTEM-------------------")

Label(root, text="Product Name: ").grid(row=1, column=0, sticky=W, padx=13, pady=5)
Label(root, text="Product Price: ").grid(row=2, column=0, sticky=W, padx=13, pady=5)
Label(root, text="Product Quantity: ").grid(row=3, column=0, sticky=W, padx=13, pady=5)

i1 = Entry(root, width=45)
i1.grid(row=1, column=1, sticky=W, padx=10, pady=5, columnspan=2)

i2 = Entry(root, width=45)
i2.grid(row=2, column=1, sticky=W, padx=10, pady=5, columnspan=2)

i3 = Entry(root, width=45)
i3.grid(row=3, column=1, sticky=W, padx=10, pady=5, columnspan=2)

b1 = Button(root, text="ADD ITEM ", width=15, command=addItem)
b1.grid(row=4, column=2, sticky=E, padx=10, pady=5)

organizer = Canvas(root, height=100, width=420)
addHeaders()

root.mainloop()
