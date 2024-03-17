def calculate_discount(total_amount, item_type):
    if item_type == "A":
        if total_amount < 100:
            raise ValueError("Invalid total amount")
        elif total_amount <= 100000:
            discount = 0
        elif total_amount <= 500000:
            discount = 0.05
        elif total_amount <= 1000000:
            discount = 0.1
        else:
            discount = 0.15
    elif item_type == "B":
        if total_amount < 100:
            raise ValueError("Invalid total amount")
        elif total_amount <= 100000:
            discount = 0.01
        elif total_amount <= 500000:
            discount = 0.07
        elif total_amount <= 1000000:
            discount = 0.12
        else:
            discount = 0.18
    else:
        raise ValueError("Invalid item type")

    return discount * total_amount