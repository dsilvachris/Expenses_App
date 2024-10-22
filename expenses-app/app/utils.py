from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(filename, data):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Expense Report")
    
    y = 700
    for line in data:
        c.drawString(100, y, line)
        y -= 20

    c.save()
