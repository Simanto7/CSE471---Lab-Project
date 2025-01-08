from xhtml2pdf import pisa
from django.template.loader import render_to_string
from io import BytesIO

def generate_invoice(order,shipping_address):
    # Render HTML content from template
    html_content = render_to_string('accounts/invoice_template.html', {'order': order, 'shipping_address': shipping_address})
    
    # Create PDF from HTML content
    pdf_io = BytesIO()
    pisa.CreatePDF(html_content, dest=pdf_io)
    pdf_io.seek(0)
    
    return pdf_io.read()  # Return PDF content
