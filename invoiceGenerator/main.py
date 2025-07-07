from fpdf import FPDF

from datetime import datetime

# =========== PDF Templates =============

class InvoicePDF(FPDF):
    def header(self):
        self.set_font('Arial','B',14)
        self.cell(0, 10, 'INVOICE', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')


### Function to collect items
def get_items_from_user():
    items=[]
    print("\nEnter item details (type 'done') to finish")

    while True:
        name=input("Item name: ")
        if name.lower()=='done':
            break
        try:
            qty=int(input("Quantity: "))
            price=float(input("Price per unit: "))
            items.append((name,qty,price))
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers for quantity and price.")
    return items


def generate_invoice(customer_name,items):
    pdf=InvoicePDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    #Customer Info
    pdf.cell(0, 10, f'Date: {datetime.now().strftime("%Y-%m-%d")}', ln=True)
    pdf.cell(0, 10, f'Customer: {customer_name}', ln=True)
    pdf.ln(10)

     # Table Headers
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80, 10, 'Item', 1)
    pdf.cell(30, 10, 'Qty', 1)
    pdf.cell(40, 10, 'Price', 1)
    pdf.cell(40, 10, 'Total', 1)
    pdf.ln()

    # Table Content
    pdf.set_font('Arial','',12)
    grand_total=0

    for name,qty,price in items:
        total=qty*price
        grand_total+=total
        pdf.cell(80, 10, name, 1)
        pdf.cell(30, 10, str(qty), 1)
        pdf.cell(40, 10, f"{price:.2f}", 1)
        pdf.cell(40, 10, f"{total:.2f}", 1)
        pdf.ln()

    # Grand Total
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(150, 10, 'Grand Total', 1)
    pdf.cell(40, 10, f"{grand_total:.2f}", 1)


    filename = f"invoice_{customer_name.replace(' ', '_')}.pdf"
    pdf.output(filename)
    print(f"\n✅ Invoice saved as '{filename}'")




###### MAIN PROGRAM
def main():
    print("Welcome to Invoice generator: ")
    Customer_name=input("Enter customer name : ")
    items=get_items_from_user()
    if items:
        generate_invoice(Customer_name,items)
    else:
        print("❗No items entered.Invoice not created.")

if __name__=="__main__":
    main()

