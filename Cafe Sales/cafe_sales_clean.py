import csv
from itertools import product
def safe_type(x):
    try:
        x = str(x)
        if "." in x:
            return float(x)
        else:
            return int(x)
    except:
        return None
def parse(dirty):
    clean_rows = []
    for row in dirty:
        clean_rows.append({
            "Transaction_ID": (row.get("Transaction ID") or "").strip(),
            "Product": (row.get("Item") or "").strip(),
            "Quantity": safe_type((row.get("Quantity") or "").strip()),
            "Price": safe_type((row.get("Price Per Unit") or "").strip()),
            "Total": safe_type((row.get("Total Spent") or "").strip()),
            "Payment_Method": (row.get("Payment Method") or "").strip(),
            "Location": (row.get("Location") or "").strip(),
            "Transaction_Date": (row.get("Transaction Date") or "").strip()
            })
    return clean_rows
def valid(value):
    return value not in {"UNKNOWN", "ERROR", "", None} and str(value).strip() != ""
def dataset_length(data: list):
    return len(data)
def rows_after_cleaning(data: list):
    k = 0
    for i in range(0, len(data)):
        if data[i]["Transaction_ID"].startswith("TXN_"):
            if valid(data[i]["Product"]):
                if data[i]["Quantity"] is not None and isinstance(data[i]["Quantity"], int):
                    if data[i]["Price"] is not None and (isinstance(data[i]["Price"], int) or isinstance(data[i]["Price"], float)):
                        if data[i]["Total"] is not None and (isinstance(data[i]["Total"], int) or isinstance(data[i]["Total"], float)):
                            if valid(data[i]["Payment_Method"]):
                                if valid(data[i]["Location"]):
                                    if valid(data[i]["Transaction_Date"]):
                                        k += 1
    return k
def total_sales_price(data: list):
    total_price = 0
    for i in range(0, len(data)):
        if isinstance(data[i]["Total"], int) or isinstance(data[i]["Total"], float):
            total_price += data[i]["Total"]
    return total_price
def total_sales_amount(data: list):
    total_amount = 0
    for i in range(0, len(data)):
        if isinstance(data[i]["Quantity"], int):
            total_amount += data[i]["Quantity"]
    return total_amount
def most_popular_product(data: list):
    product_frequencies = {"Coffee": 0, "Cake": 0, "Cookie": 0, "Salad": 0, "Smoothie": 0, "Sandwich": 0, "Juice": 0, "Tea": 0, }
    for i in range(0, len(data)):
        product = data[i]["Product"]
        if valid(product):
            product = product.strip().title()
            if product in product_frequencies:
                product_frequencies[product] += 1
    max_value = max(product_frequencies.values())
    for i in product_frequencies.keys():
        if product_frequencies[i] == max_value:
            return i
def data_problems_analyzer(data: list):
    missing_product_name = []
    missing_price = []
    missing_quantity = []
    negative_price = []
    negative_quantity = []
    zero_quantity = []
    unusual_total = []
    for i in range(0, len(data)):
        if not valid(data[i]["Product"]):
            missing_product_name.append(i)
        if not valid(data[i]["Price"]):
            missing_price.append(i)
        if not valid(data[i]["Quantity"]):
            missing_quantity.append(i)
        if valid(data[i]["Price"]) and valid(data[i]["Quantity"]) and valid(data[i]["Location"]) and valid(data[i]["Payment_Method"]) and valid(data[i]["Product"]) and valid(data[i]["Total"]) and valid(data[i]["Transaction_Date"]):
            if data[i]["Price"] < 0:
                negative_price.append(i)
            if data[i]["Quantity"] < 0:
                negative_quantity.append(i)
            if data[i]["Quantity"] == 0:
                zero_quantity.append(i)
            if (isinstance(data[i]["Total"], (int, float)) and isinstance(data[i]["Price"], (int, float)) and isinstance(data[i]["Quantity"], (int, float))) and data[i]["Total"] != data[i]["Price"] * data[i]["Quantity"]:
                unusual_total.append(i)
    print(f"Missing product name: {missing_product_name}.")
    print(f"Missing price: {missing_price}.")
    print(f"Missing quantity: {missing_quantity}.")
    print(f"Negative price: {negative_price}.")
    print(f"Negative quantity: {negative_quantity}.")
    print(f"Zero quantity: {zero_quantity}.")
    print(f"Unusual total: {unusual_total}.")
          
dirty_data = []
with open("dirty_cafe_sales.csv", mode="r") as file:
    reader = csv.DictReader(file)
    dirty_data.extend(parse(reader))
print("The length of the dataset is {}.".format(dataset_length(dirty_data)))
print("There are {} rows valid after cleaning.".format(rows_after_cleaning(dirty_data)))
print(f"The total sales price is {total_sales_price(dirty_data)}.")
print(f"The total sales quantity is {total_sales_amount(dirty_data)}.")
print(f"The most popular product is {most_popular_product(dirty_data)}.")
data_problems_analyzer(dirty_data)
            