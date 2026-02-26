import re
import json

def parse_receipt(file_path):
    # Read the raw receipt text
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # --- 1. Extract date and time ---
    date_time_match = re.search(r'(\d{2}\.\d{2}\.\d{4}) (\d{2}:\d{2}:\d{2})', text)
    date_time = None
    if date_time_match:
        date, time = date_time_match.groups()
        # Format as ISO style
        date_time = f"{date.split('.')[2]}-{date.split('.')[1]}-{date.split('.')[0]}T{time}"

    # --- 2. Extract payment method ---
    payment_match = re.search(r'Банковская карта|Наличные|Cash|Card', text, re.IGNORECASE)
    payment_method = payment_match.group() if payment_match else None

    # --- 3. Extract items ---
    # Pattern: Name + quantity x price + total_price (Стоимость)
    item_pattern = re.compile(
        r'(?P<name>.+?)\n(?P<quantity>\d+),?0*\s*x\s*(?P<unit_price>[\d\s]+,\d{2})\n(?P<total_price>[\d\s]+,\d{2})',
        re.MULTILINE
    )
    
    items = []
    for match in item_pattern.finditer(text):
        name = match.group("name").strip()
        quantity = int(match.group("quantity"))
        # Convert prices from string "1 152,00" -> float 1152.00
        unit_price = float(match.group("unit_price").replace(" ", "").replace(",", "."))
        total_price = float(match.group("total_price").replace(" ", "").replace(",", "."))
        
        items.append({
            "name": name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        })
    
    # --- 4. Extract total amount ---
    total_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
    total = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else None

    # --- 5. Extract store info ---
    store_match = re.search(r'Филиал\s+(.+)', text)
    store = store_match.group(1).strip() if store_match else None

    # --- 6. Build final structured output ---
    receipt_data = {
        "store": store,
        "date_time": date_time,
        "payment_method": payment_method,
        "items": items,
        "total": total
    }

    # Output as pretty JSON
    print(json.dumps(receipt_data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    # Replace 'raw.txt' with your receipt file
    parse_receipt("raw.txt")