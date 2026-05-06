import tkinter as tk
from tkinter import messagebox

#First Class
class Order:
    def __init__(self, name, age, drink, size, price):
        self.name = name
        self.age = age
        self.drink = drink
        self.size = size
        self.price = price
#Where the information is saved so that it is not lost when it is closed
    def save_to_file(self):
        with open("orders.txt", "a") as f:
            f.write(f"{self.name}, {self.age}, {self.drink}, {self.size}, ${self.price}\n")

#The menu that has all of our available drinks
prices = {
    "Coke": {"Small": 3, "Medium": 4, "Large": 5},
    "Juice": {"Small": 4, "Medium": 5, "Large": 6},
    "Water": {"Small": 2, "Medium": 3, "Large": 4},
    "Beer": {"Small": 6, "Medium": 8, "Large": 10},
    "Wine": {"Small": 7, "Medium": 9, "Large": 11},
    "Vodka": {"Small": 8, "Medium": 10, "Large": 12},
    "Whiskey": {"Small": 9, "Medium": 11, "Large": 13},
    "Rum": {"Small": 8, "Medium": 10, "Large": 12},
    "Gin": {"Small": 8, "Medium": 10, "Large": 12},
    "Margarita": {"Small": 10, "Medium": 12, "Large": 14},
    "Mojito": {"Small": 10, "Medium": 12, "Large": 14},
    "Piña Colada": {"Small": 11, "Medium": 13, "Large": 15},
    "Espresso Martini": {"Small": 12, "Medium": 14, "Large": 16}
}

#The fist function that will allow the user to place the order and also check if the user is old enough to order as well as calculate the price of the order and save it to a file
def place_order():
    name = name_entry.get()
    age = age_entry.get()
    drink = drink_var.get()
    size = size_var.get()
#Checking for blank input fields
    if name == "" or age == "":
        messagebox.showerror("You have not filled in all of the required fields, please try again")
        return
#Checkung for the valid age of the user ensuring that it is an integer and that they are the right age to order alcohol
    try:
        age = int(age)
    except:
        messagebox.showerror("You need to enter a number into the age box, please try again")
        return
#
    if age < 18:
        messagebox.showerror("You need to be 18+ to order, please do not break the law and try again when you are of age")
        return

    price = prices[drink][size]
#Creatim=ng the order object and saving it to a file
    order = Order(name, age, drink, size, price)
    order.save_to_file()

    messagebox.showinfo("Yayyy, you have succesfully had your", f"Order placed!\nTotal: ${price}")

#The GUI for my menu system that will ask the user for their, name, age, drink and size of the drink where I use a button to allow them to palce their order
root = tk.Tk()
root.title("Drink Ordering System")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

#The dropdpwn of the different drinks which are automatically added from my prices dictionary so that if I add a new drink to my menu it will automatically be added to the dropdown without me having to keep on cahnging my codded
drink_var = tk.StringVar(value="Coke")
tk.Label(root, text="Driink").pack()

drink_options = list(prices.keys()) 
tk.OptionMenu(root, drink_var, *drink_options).pack()

#The different size options for the customer to choose from
size_var = tk.StringVar(value="Small")
tk.Label(root, text="Size").pack()
#Radiobuttons that are used for the different size options that are ther to choose from
tk.Radiobutton(root, text="Smal", variable=size_var, value="Small").pack()
tk.Radiobutton(root, text="Medium", variable=size_var, value="Medium").pack()
tk.Radiobutton(root, text="Large", variable=size_var, value="Large").pack()

#Final button for the user which they can use to place their order
tk.Button(root, text="Place my order", command=place_order).pack()

root.mainloop()