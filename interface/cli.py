def get_input():

    data = {}

    data["product_cost"] = float(input("Product Cost: "))
    data["freight"] = float(input("Freight Cost: "))
    data["insurance"] = float(input("Insurance Cost: "))
    data["duty_rate"] = float(input("Import Duty (%): ")) / 100
    data["vat_rate"] = float(input("VAT (%): ")) / 100
    data["port_charge"] = float(input("Port Charges: "))
    data["logistics"] = float(input("Local Logistics: "))
    data["quantity"] = int(input("Quantity: "))
    data["selling_price"] = float(input("Selling Price per Unit: "))

    return data
