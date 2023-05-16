import datetime
import tkinter as tk
from tkinter import messagebox

# Dictionary of available products and their prices
products = {
    'Product 1': {'price': 50},
    'Product 2': {'price': 100},
    'Product 3': {'price': 150},
    'Product 4': {'price': 200},
    'Product 5': {'price': 250}
}

bill_number = 1


# Function to calculate the total price and discount
def calculate_bill():
    global bill_number
    if bill_number > 2:
        messagebox.showwarning('bill_number', 'bill_number exceeded 30 bills')
    else:
        name = name_entry.get()
        phone = phone_entry.get()
        product1_amount = int(product1_entry.get())
        product2_amount = int(product2_entry.get())
        product3_amount = int(product3_entry.get())
        product4_amount = int(product4_entry.get())
        product5_amount = int(product5_entry.get())

        total_price = 0
        total_price += products['Product 1']['price'] * product1_amount
        total_price += products['Product 2']['price'] * product2_amount
        total_price += products['Product 3']['price'] * product3_amount
        total_price += products['Product 4']['price'] * product4_amount
        total_price += products['Product 5']['price'] * product5_amount

        # Calculate discount
        discount = 0
        if 100 <= total_price <= 199:
            discount = total_price * 0.05
        elif 200 <= total_price <= 299:
            discount = total_price * 0.1
        elif total_price >= 300:
            discount = total_price * 0.1

        # Calculate total price after discount
        total_price_after_discount = total_price - discount

        # Generate the bill
        bill_text = f"Date: {current_date}\nBill Number: {bill_number}\n\n"
        bill_text += f"Name: {name}\nPhone: {phone}\n\n"

        for product, amount_entry in zip(products,
                                         [product1_entry, product2_entry, product3_entry, product4_entry,
                                          product5_entry]):
            amount = int(amount_entry.get())
            price = products[product]['price']
            total_product_price = price * amount
            bill_text += f"Product: {product}\n"
            bill_text += f"Price: {price}\nAmount: {amount}\n"
            bill_text += f"Total Price: {total_product_price}\n\n"

        bill_text += f"Total Price: {total_price}\nDiscount: {discount}\n"
        bill_text += f"Total Price After Discount: {total_price_after_discount}"

        bill_number += 1
        messagebox.showinfo("Bill", bill_text)


# Generate bill number and current date (you can use your own method to generate bill number)
current_date = datetime.date.today()

# Create the main Tkinter window
window = tk.Tk()
window.title("Bill Calculator")
window.geometry("400x450")
window.configure(background='#222831')

# Create labels and entry fields
name_label = tk.Label(window, text="Name:", bg='#222831', fg='#EEEEEE')
name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(window, text="Phone:", bg='#222831', fg='#EEEEEE')
phone_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
phone_entry = tk.Entry(window)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

product1_label = tk.Label(window, text="Product 1 amount:", bg='#222831', fg='#EEEEEE')
product1_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
product1_entry = tk.Entry(window)
product1_entry.grid(row=2, column=1, padx=10, pady=10)

product2_label = tk.Label(window, text="Product 2 amount:", bg='#222831', fg='#EEEEEE')
product2_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
product2_entry = tk.Entry(window)
product2_entry.grid(row=3, column=1, padx=10, pady=10)

product3_label = tk.Label(window, text="Product 3 amount:", bg='#222831', fg='#EEEEEE')
product3_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
product3_entry = tk.Entry(window)
product3_entry.grid(row=4, column=1, padx=10, pady=10)

product4_label = tk.Label(window, text="Product 4 amount:", bg='#222831', fg='#EEEEEE')
product4_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
product4_entry = tk.Entry(window)
product4_entry.grid(row=5, column=1, padx=10, pady=10)

product5_label = tk.Label(window, text="Product 5 amount:", bg='#222831', fg='#EEEEEE')
product5_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
product5_entry = tk.Entry(window)
product5_entry.grid(row=6, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate Bill", command=calculate_bill, bg='#00ADB5', fg='#EEEEEE')
calculate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Configure grid weights to make the widgets expandable
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(8, weight=1)

# Run the main Tkinter event loop
window.mainloop()
