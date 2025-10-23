import pdfplumber
import re

def extract_data_points(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                text += txt
        last_four_digits = re.search(r'(\d{4})$', text)
        transaction_info = re.findall(r'Transaction\s*:\s*(.*)', text)
        billing_cycle = re.search(r'Billing Cycle:\s*(\d{2}/\d{2}/\d{4}) - (\d{2}/\d{2}/\d{4})', text)
        payment_due_date = re.search(r'Due Date:\s*(\d{2}/\d{2}/\d{4})', text)
        total_balance = re.search(r'Total Outstanding:\s*([\d,]+.\d{2})', text)
        return {
            "last_four_digits": last_four_digits.group(1) if last_four_digits else "",
            "transactions": transaction_info if transaction_info else [],
            "billing_cycle": billing_cycle.groups() if billing_cycle else "",
            "payment_due_date": payment_due_date.group(1) if payment_due_date else "",
            "total_balance": total_balance.group(1) if total_balance else "",
        }
