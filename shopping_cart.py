# shopping_cart.py

#from pprint import pprint
import datetime

#read from CSV file
import csv

#what my csv file is saved as
csv_file_path = "products.csv"

#this probably opens the csv file
with open(csv_file_path, "r") as csv_file: 
    reader = csv.DictReader(csv_file)
    #for row in reader:
    #print(row["id"], row["name"])
    #for rows in reader:
    #    id = rows[0]
    #    name = rows[1]
    #    price = rows[2]
    #products = {id:price for id, name, price in rows}
   # print(products)


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


# TODO: write some Python code here to produce the desired output


#
# INFO CAPTURE (INPUT)
#
total_price = 0
sales_tax = 0
tax_percentage = .0875
real_total = 0
selected_ids = [] #create a list of ids selected

valid_ids = [] #list of valid ids from the list
for p in products:
    valid_ids.append(p["id"]) 



while True:
    #get the input
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ") #this is a string

    if selected_id == "DONE":
        break
    elif int(selected_id) in valid_ids:
        selected_ids.append(selected_id)
    else:
        print("Hey, are you sure that product identifier is correct? Please try again!") #error message


# INFO DISPLAY (OUTPUT)
#

#for selected_id in selected_ids:
#    matching_products = [p for p in products if str(p["id"])  == str(selected_id)]
#    matching_product = matching_products[0]
#    total_price = total_price + matching_product["price"]
#    print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))


#starting the receipt
print("--------------------------------")
print("~~~~~~~SAMAR'S STUFF~~~~~~~~~")
print("phone number: 856-333-7979")
print("www.samarstuff.com")
print("--------------------------------")

#date time goes here
today = datetime.datetime.today()
print("CHECKOUT AT: ")
print(today.strftime("%Y-%m-%d %I:%M %p"))

print("--------------------------------")


#selected items
print("SELECTED PRODUCTS:")
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"])  == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    selected_product_price = "${0:.2f}".format(matching_product["price"])
    print("... " + matching_product["name"] + " " + "(" + selected_product_price + ")")


print("--------------------------------")


#do my calculations
sales_tax = total_price * tax_percentage
real_total = total_price + sales_tax


#now I am printing the total
total_price = "${0:.2f}".format(total_price)
print("TOTAL PRICE: " + total_price) 
sales_tax = "${0:.2f}".format(sales_tax)
print("SALES TAX: " + sales_tax)
real_total = "${0:.2f}".format(real_total)
print("TOTAL OWED: " + real_total)
print("--------------------------------")


#now for a friendly message
print("THANK YOU FOR SHOPPING AT SAMAR'S STUFF!")
print("HAVE A GREAT DAY")