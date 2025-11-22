import re
from typing import List, Dict

class LineItem:
    def __init__(self, description: str, quantity: int, unit_price: float, total: float):
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
        self.total = total

class Invoice:
    def __init__(self):
        self.invoice_id = None
        self.invoice_date = None
        self.supplier_name = None
        self.currency = None
        self.subtotal = None
        self.tax = None
        self.total = None
        self.line_items: List[LineItem] = []
        self.due_date = None
        self.po_number = None
        self.issues: List[str] = []
        self.confidence: Dict[str, float] = {}
        self.anchors: Dict[str, str] = {}

def extract_invoice(text: str) -> Invoice:
    inv = Invoice()
    # Example regex for invoice ID
    match = re.search(r"Invoice[:\s]+(\S+)", text)
    if match:
        inv.invoice_id = match.group(1)
        inv.confidence["invoice_id"] = 0.9
        inv.anchors["invoice_id"] = match.group(0)
    else:
        inv.issues.append("Missing invoice ID")
        inv.confidence["invoice_id"] = 0.0
    # Add more extraction logic here...
    return inv
