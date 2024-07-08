from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_receipt(customer_name, amount, transaction_id, items, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a PDF with ReportLab
    pdf_file = os.path.join(output_dir, f"receipt_{transaction_id}.pdf")
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    # Add some text to the PDF
    c.setFont("Helvetica", 12)

    # Title
    c.drawString(200, height - 50, "Payment Receipt")

    # Customer Information
    c.drawString(50, height - 100, f"Customer Name: {customer_name}")
    c.drawString(50, height - 120, f"Transaction ID: {transaction_id}")
    c.drawString(50, height - 140, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Items
    c.drawString(50, height - 180, "Items Purchased:")
    y_position = height - 200
    for item, price in items.items():
        c.drawString(60, y_position, f"{item}: ${price:.2f}")
        y_position -= 20

    # Total Amount
    c.drawString(50, y_position - 20, f"Total Amount: ${amount:.2f}")

    # Thank You Note
    c.drawString(50, y_position - 60, "Thank you for your purchase!")

    # Save the PDF
    c.save()
    return pdf_file

# Example usage
customer_name = "P.suhas"
amount = 123.45
transaction_id = "suhas185"
items = {
    "Item 1": 100.00,
    "Item 2": 300.00,
    "Item 3": 480.45,
    "Item 4": 200.00,
}

output_dir = "C:\\Users\\suhas\\Downloads\\cipher bites"
pdf_path = generate_receipt(customer_name, amount, transaction_id, items, output_dir)
print(f"Receipt saved as {pdf_path}")
