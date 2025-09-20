import re
import pandas as pd
from .utils import extract_text

def extract_date_safe(text: str) -> str:
    for line in text.split('\n')[:10]:
        match = re.search(r'(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})', line)
        if match:
            return match.group(1)
    return None

def parse_invoice_header_safe(text: str) -> dict:
    data = {"Invoice_No": None, "Date": None, "Total": None}
    lines = text.split('\n')

    # Invoice Number
    for line in lines[:10]:
        if 'invoice' in line.lower():
            match = re.search(r'\b\d{3,20}\b', line)
            if match:
                data["Invoice_No"] = match.group(0)
                break

    # Date
    data["Date"] = extract_date_safe(text)

    # Total
    total_match = re.findall(r'total[:\s$]*([\d.,]+)', text, re.IGNORECASE)
    data["Total"] = total_match[-1] if total_match else None

    return data

def parse_line_items(text: str) -> pd.DataFrame:
    lines = text.split('\n')
    items = []
    stop_keywords = ['subtotal', 'total', 'tax', 'invoice', 'payment', 'account']

    for line in lines:
        line = line.strip()
        if not line or 'description' in line.lower() or 'product' in line.lower():
            continue
        if any(k in line.lower() for k in stop_keywords):
            continue

        line_clean = line.replace('$', ' ').replace('\t',' ').replace('  ',' ')
        match = re.match(r'(.+?)\s+(\d+)\s+([\d,.]+)\s+([\d,.]+)', line_clean)
        if match:
            desc, qty, unit_price, amount = match.groups()
            items.append({
                "Description": desc.strip(),
                "Quantity": qty,
                "Unit Price": unit_price,
                "Amount": amount
            })

    return pd.DataFrame(items)
