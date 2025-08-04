import tkinter as tk
from tkinter import messagebox from datetime import datetime


class IceCreamShop(tk.Tk): def init(self):
super().init()
self.title("D CUBE ICECREAMS") self.geometry("800x700")
self.configure(bg="orange") # Set background color to orange

# Initialize variables
self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Blueberry', 'Butter Pecan', 'Coffee',
 'Rocky Road', 'Cookies and Cream', 'Pistachio']
self.toppings = ['Chocolate Chips', 'Sprinkles', 'Whipped Cream', 'Cherries', 'Caramel Sauce'
, 'Hot Fudge',
'Nuts', 'Marshmallows', 'Cookie Dough', 'Toffee Bits', 'Gummy Bears', 'Brownie
Bits', 'Fruit',
'Granola', 'Coconut Flakes']
self.milkshakes = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Blueberry', 'Banana', 'Coffee',
 'Peanut Butter', 'Oreo', 'Caramel', 'Mocha', 'Pineapple', 'Raspberry', 'Peach',
'Watermelon',
'Mango', 'Kiwi', 'Passion Fruit', 'Guava', 'Pomegranate']
self.icecream_cakes = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Blueberry', 'Butter Pecan', 'Coffee',
'Rocky Road', 'Cookies and Cream', 'Pistachio'] self.inventory = {flavor: 100000 for flavor in self.flavors} self.order_total = 0

# Rates (in Indian Rupees) self.flavor_rate = 50
self.topping_rate = 20
self.milkshake_rate = 45
self.cake_rate = 70

# Create frame for left side elements self.left_frame = tk.Frame(self, bg="#7FFFD4")
self.left_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=10)

# Create frame for right side elements self.right_frame = tk.Frame(self, bg="#7FFFD4")
self.right_frame.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=10) # Ice Cream Shop Title
 
self.title_label = tk.Label(self.left_frame, text="D CUBE ICECREAMS", bg="#FFFF00", fg="#0000FF",
font=("Helvetica", 20, "bold")) self.title_label.pack(pady=10)

# Create GUI elements for Ice Cream
self.flavor_label = tk.Label(self.left_frame, text="Select Ice Cream Flavor:", bg="#7FFFD4",
font=("Helvetica", 12)) self.flavor_label.pack(pady=10)

self.flavor_var = tk.StringVar(self.left_frame) self.flavor_var.set(self.flavors[0]) # Default flavor
self.flavor_menu = tk.OptionMenu(self.left_frame, self.flavor_var, *self.flavors) self.flavor_menu.config(bg="white")
self.flavor_menu.pack()

self.quantity_label = tk.Label(self.left_frame, text="Quantity:", bg="#7FFFD4", 
font=("Helvetica", 12))
self.quantity_label.pack(pady=10)

self.quantity_entry = tk.Entry(self.left_frame) self.quantity_entry.pack()

self.toppings_label = tk.Label(self.left_frame, text="Select Toppings:", bg="#7FFFD4", font=("Helvetica", 12))
self.toppings_label.pack(pady=10)

self.toppings_var = tk.StringVar(self.left_frame) self.toppings_var.set("None")
self.toppings_menu = tk.OptionMenu(self.left_frame, self.toppings_var, *self.toppings) self.toppings_menu.config(bg="white")
self.toppings_menu.pack()

# Create GUI elements for Milkshakes
self.milkshake_label = tk.Label(self.left_frame, text="Select Milkshake Flavor:",
 bg="#7FFFD4",
font=("Helvetica", 12)) self.milkshake_label.pack(pady=10)

self.milkshake_var = tk.StringVar(self.left_frame) self.milkshake_var.set(self.milkshakes[0]) # Default milkshake flavor self.milkshake_menu = tk.OptionMenu(self.left_frame, self.milkshake_var,
*self.milkshakes) self.milkshake_menu.config(bg="white") self.milkshake_menu.pack()

self.milkshake_quantity_label = tk.Label(self.left_frame, text="Quantity:", bg="#7FFFD4", font=("Helvetica", 12))
self.milkshake_quantity_label.pack(pady=10)
 
self.milkshake_quantity_entry = tk.Entry(self.left_frame) self.milkshake_quantity_entry.pack()

# Create GUI elements for Ice Cream Cakes
self.cake_label = tk.Label(self.left_frame, text="Select Ice Cream Cake Flavor:", bg="#7FFFD4",
font=("Helvetica", 12)) self.cake_label.pack(pady=10)

self.cake_var = tk.StringVar(self.left_frame) self.cake_var.set(self.icecream_cakes[0]) # Default cake flavor
self.cake_menu = tk.OptionMenu(self.left_frame, self.cake_var, *self.icecream_cakes) self.cake_menu.config(bg="white")
self.cake_menu.pack()

self.cake_quantity_label = tk.Label(self.left_frame, text="Quantity:", bg="#7FFFD4", font=("Helvetica", 12))
self.cake_quantity_label.pack(pady=10)

self.cake_quantity_entry = tk.Entry(self.left_frame) self.cake_quantity_entry.pack()

# Customer Details
self.name_label = tk.Label(self.right_frame, text="Enter Your Name:", bg="#7FFFD4", font=("Helvetica", 12))
self.name_label.pack(pady=10)

self.name_entry = tk.Entry(self.right_frame) self.name_entry.pack()

self.mobile_label = tk.Label(self.right_frame, text="Enter Your Mobile Number:",
 bg="#7FFFD4",
font=("Helvetica", 12)) self.mobile_label.pack(pady=10)

self.mobile_entry = tk.Entry(self.right_frame) self.mobile_entry.pack()

self.add_to_order_button = tk.Button(self.right_frame, text="Add to Cart", command=self.add_to_order,
bg="orange", font=("Helvetica", 12)) self.add_to_order_button.pack(pady=10)

self.view_order_button = tk.Button(self.right_frame, text="View Invoice", command=self.generate_invoice,
bg="orange", font=("Helvetica", 12)) self.view_order_button.pack(pady=10)

# Order History
self.order_history_label = tk.Label(self.right_frame, text="Order History:", bg="white", font=("Helvetica", 12))
 
self.order_history_label.pack(pady=10)

self.order_history_frame = tk.Frame(self.right_frame) self.order_history_frame.pack(pady=5)

self.order_history_text = tk.Text(self.right_frame, bg="black", fg="white",
 font=("Helvetica", 10),
height=20, width=40, wrap="word", state="disabled") self.order_history_text.pack()

def add_to_order(self):
flavor = self.flavor_var.get() toppings = self.toppings_var.get() try:
quantity = int(self.quantity_entry.get()) if quantity <= self.inventory[flavor]:
self.inventory[flavor] -= quantity
self.order_total += quantity * self.flavor_rate # Calculate cost based on rate messagebox.showinfo("Success", f"{quantity} {flavor} with {toppings} toppings
added to order.")
self.update_order_history(f"{quantity} {flavor} with {toppings} toppings") else:
messagebox.showerror("Error", "Insufficient inventory.") except ValueError:
messagebox.showerror("Error", "Invalid quantity.")

rate
 
# Add Milkshake Order
milkshake_flavor = self.milkshake_var.get() try:
milkshake_quantity = int(self.milkshake_quantity_entry.get())
self.order_total += milkshake_quantity * self.milkshake_rate # Calculate cost based on

messagebox.showinfo("Success", f"{milkshake_quantity} {milkshake_flavor}
 
milkshakes added to order.")
self.update_order_history(f"{milkshake_quantity} {milkshake_flavor} milkshakes") except ValueError:
messagebox.showerror("Error", "Invalid milkshake quantity.")

# Add Ice Cream Cake Order cake_flavor = self.cake_var.get() try:
cake_quantity = int(self.cake_quantity_entry.get())
self.order_total += cake_quantity * self.cake_rate # Calculate cost based on rate messagebox.showinfo("Success", f"{cake_quantity} {cake_flavor} ice cream cakes
added to order.")
self.update_order_history(f"{cake_quantity} {cake_flavor} ice cream cakes") except ValueError:
messagebox.showerror("Error", "Invalid cake quantity.")

def generate_invoice(self): name = self.name_entry.get()
 
mobile = self.mobile_entry.get()
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
invoice_details = f"Date and Time: {date_time}\nCustomer Name: {name}\nMobile Number: {mobile}\n\nOrder Summary:\n"
for flavor, quantity in self.inventory.items(): invoice_details += f"{flavor}: {quantity}\n"
invoice_details += f"\nTotal amount: ₹ {self.order_total}" # Display total amount in Indian
 Rupees
messagebox.showinfo("Invoice", invoice_details)

def update_order_history(self, order): self.order_history_text.config(state="normal") self.order_history_text.insert(tk.END, f"{order}\n") self.order_history_text.config
(state="disabled")

