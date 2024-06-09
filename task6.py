def calculate_road_tax(cost_price):
    if cost_price > 100000:
        tax_percentage = 15
    elif cost_price > 50000:
        tax_percentage = 10
    else:
        tax_percentage = 5
    
    road_tax = (cost_price * tax_percentage) / 100
    return road_tax

def main():
    cost_price = float(input("Enter the cost price of the bike (in Rs): "))
    road_tax = calculate_road_tax(cost_price)
    print(f"The road tax to be paid is: Rs {road_tax:.2f}")

if __name__ == "__main__":
    main()
