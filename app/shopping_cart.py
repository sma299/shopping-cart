# shopping_cart.py

# from pprint import pprint
import datetime # get the date and time
import os # need this to write to a file


# HERE I WILL PUT MY NEW FUNCTIONS because I cannot repeat myself!

"""
my first docstring comment
converts a numeric value to usd-formatted string, for printing and display purposes
"""

def to_usd(amount):
    return "${0:,.2f}".format(amount)

"""
datetime function that returns the date in this format
ex: 2020-04-10 02:36 PM
""" 

def human_friendly_timestamp():
    today = datetime.datetime.today()
    checkout_at = today.strftime("%Y-%m-%d %I:%M %p")
    return checkout_at

"""
product lookup function that finds and returns the proper product, even if the products are not sorted in order of their unique identifiers. 
""" 

def find_product(selected_id, products):
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    return matching_product

if __name__ == "__main__":

    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


    #
    # INFO CAPTURE (INPUT)
    #
    total_price = 0
    sales_tax = 0
    tax_percentage = .0875
    real_total = 0
    selected_ids = [] # create a list of ids selected

    valid_ids = [] # list of valid ids from the list
    for p in products:
        valid_ids.append(p["id"]) 



    while True:
        # get the input
        selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ") # this is a string

        if selected_id == "DONE":
            break
        elif int(selected_id) in valid_ids:
            selected_ids.append(selected_id)
        else:
            print("Hey, are you sure that product identifier is correct? Please try again!") # error message


    # INFO DISPLAY (OUTPUT)

    receipt = ""

    # starting the receipt
    receipt += "\n--------------------------------"
    receipt += "\n~~~~~~~SAMAR'S STUFF~~~~~~~~~"
    receipt += "\nphone number: 856-333-7979"
    receipt += "\nwww.samarstuff.com"
    receipt += "\n--------------------------------"

    # date time goes here
    receipt += "\nCHECKOUT AT: "
    receipt += "\n" + human_friendly_timestamp()

    receipt += "\n--------------------------------"


    # selected items
    receipt += ("\nSELECTED PRODUCTS:")
    for selected_id in selected_ids:
        # I use a function here!
        matching_product = find_product(selected_id, products)
        total_price = total_price + matching_product["price"]
        selected_product_price = to_usd(matching_product["price"])
        receipt += "\n" + "... " + matching_product["name"] + " " + "(" + selected_product_price + ")"


    receipt += "\n--------------------------------"


    # do my calculations
    sales_tax = total_price * tax_percentage
    real_total = total_price + sales_tax


    # now I am printing the total
    receipt += "\nTOTAL PRICE: " + to_usd(total_price)
    receipt += "\nSALES TAX: " + to_usd(sales_tax)
    receipt += "\nTOTAL OWED: " + to_usd(real_total)
    receipt += "\n--------------------------------"


    # now for a friendly message
    receipt += "\nTHANK YOU FOR SHOPPING AT SAMAR'S STUFF!"
    receipt += "\nHAVE A GREAT DAY"

    print(receipt)

    #file_name = os.path.join(os.path.dirname(__file__),"..", "receipts", f"{now.strftime("%Y-%M-%d-%H-%m-%S")}.txt")
    file_name = os.path.join(os.path.dirname(__file__),"..", "receipts")
    with open(file_name, 'w') as f:
        f.write(receipt)