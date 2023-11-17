
def get_value():
    """this fuction get recive the value of user for the database table"""
    product_code = input("Enter the 3 lenght value number for the product code : ")
    name = input("Enter the name for the product :  ")
    quantity = input("Enter the quantity for the product  : ")
    price = input("Enter price for the product : ")
    return product_code, name, quantity, price
