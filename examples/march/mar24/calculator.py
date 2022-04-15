def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid Price, please try again")
            
            
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter Quality: "))
            return quantity
        except ValueError:
            print("Invalid Quantity. Enter a Whole Number.")

#calculator program
price = get_price()
quantity = get_quantity()
total = price * quantity
price(f"Your total is ${total}")