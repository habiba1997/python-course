from tkinter import *
from fpdf import FPDF


def add_medicine():
    # anchor to get the selected item from list
    selected_medicine = medicine_listbox.get(ANCHOR)
    if selected_medicine:
        quantity = int(quantity_entry.get())
        price = medicines[selected_medicine]
        item_total = price * quantity
        # saved in items as a tuple
        invoice_items.append((selected_medicine, quantity, item_total))
        total_amount_entry.delete(0, END)
        total_amount_entry.insert(END, str(calculate_total()))
        update_invoice_text()


def update_invoice_text():
    # line.column from first line zero column 1.0
    # to re-add them from the start
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(
            END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")


def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total


def generate_pdf_invoice():
    customer_name = customer_entry.get()

    pdf = FPDF()
    pdf.add_page()

    # Set up PDF formatting
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, txt="Invoice", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 10, txt="Customer: " + customer_name, new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.cell(0, 10, txt="", new_x="LMARGIN", new_y="NEXT")

    # Add invoice items to PDF
    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(
            0, 10, txt=f"Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}", new_x="LMARGIN",
            new_y="NEXT", align="L")

    # Add total amount to PDF
    pdf.cell(0, 10, txt="Total Amount: " +
                        str(calculate_total()), new_x="LMARGIN", new_y="NEXT", align="L")

    # Save the PDF file
    pdf.output("invoice.pdf")


# Create the main window
window = Tk()
window.title("Invoice Generator")

# Initialize medicine dictionary carrying each medicine with its price
medicines = {
    "Medicine A": 10,
    "Medicine B": 20,
    "Medicine C": 15,
    "Medicine D": 25
}
invoice_items = []
total_amount = 0.0

# GUI layout
medicine_label = Label(window, text="Medicine:")
medicine_label.pack()

# mode single , so you can only select one item at a time
medicine_listbox = Listbox(window, selectmode=SINGLE)
for med in medicines:
    medicine_listbox.insert(END, med)
medicine_listbox.pack()

quantity_label = Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = Entry(window)
quantity_entry.pack()

add_button = Button(window, text="Add Medicine", command=add_medicine)
add_button.pack()

total_amount_label = Label(window, text="Total Amount:")
total_amount_label.pack()
total_amount_entry = Entry(window)
total_amount_entry.pack()

customer_label = Label(window, text="Customer Name:")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(
    window, text="Generate Invoice", command=generate_pdf_invoice)
generate_button.pack()

invoice_text = Text(window, height=10, width=50)
invoice_text.pack()

# Start the GUI event loop
window.mainloop()
