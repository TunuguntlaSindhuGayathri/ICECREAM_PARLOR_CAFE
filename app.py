from models import SeasonalFlavorOffering, IngredientInventory, CustomerFlavorSuggestion, AllergyConcern
from cart import Cart
from utils import fetch_all, execute_query

def main_menu(cart):
    print("Welcome to the Ice Cream Parlor Cafe")
    while True:
        print("1. View and Search Seasonal Flavor Offerings")
        print("2. View Ingredient Inventory")
        print("3. Add Customer Flavor Suggestion")
        print("4. Add Allergy Concern")
        print("5. Manage Cart")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            search_term = input("Enter flavor to search for (leave blank to view all): ")
            view_and_search_seasonal_flavor_offerings(search_term, cart)
        elif choice == '2':
            view_ingredient_inventory()
        elif choice == '3':
            add_customer_flavor_suggestion()
        elif choice == '4':
            add_allergy_concern()
        elif choice == '5':
            manage_cart(cart)
        elif choice == '6':
            print("Thank you for visiting the Ice Cream Parlor Cafe!")
            break
        else:
            print("Invalid choice. Please try again.")

def view_and_search_seasonal_flavor_offerings(search_term="", cart=None):
    if search_term:
        query = "SELECT * FROM seasonal_flavor_offerings WHERE name LIKE ?"
        params = ('%' + search_term + '%',)
    else:
        query = "SELECT * FROM seasonal_flavor_offerings"
        params = ()
    
    flavors = fetch_all(query, params)

    if flavors:
        for flavor in flavors:
            print(f"ID: {flavor[0]}, Name: {flavor[1]}, Seasonal: {flavor[2]}")
        
        print("Select an action:")
        print("1. Add to cart")
        print("2. Add to favorites")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item_to_cart(flavors, cart)
        elif choice == '2':
            add_item_to_favorites(flavors, cart)
        else:
            print("Invalid choice.")
    else:
        print("No flavors found.")
    
    return flavors

def add_item_to_cart(flavors, cart):
    item_id = input("Enter the ID of the flavor to add to cart: ")
    for flavor in flavors:
        if str(flavor[0]) == item_id:
            cart.add_item(flavor[1])
            print(f"{flavor[1]} added to cart.")
            return
    print("Invalid flavor ID.")

def add_item_to_favorites(flavors, cart):
    item_id = input("Enter the ID of the flavor to add to favorites: ")
    for flavor in flavors:
        if str(flavor[0]) == item_id:
            cart.add_favorite(flavor[1])
            print(f"{flavor[1]} added to favorites.")
            return
    print("Invalid flavor ID.")

def view_ingredient_inventory():
    query = "SELECT * FROM ingredient_inventory"
    ingredients = fetch_all(query)

    if ingredients:
        for ingredient in ingredients:
            print(f"ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]}")
    else:
        print("No ingredients found.")
    
    return ingredients

def add_customer_flavor_suggestion():
    flavor_id = input("Enter flavor ID for the suggestion: ")
    suggestion = input("Enter your suggestion: ")

    query = "INSERT INTO customer_flavor_suggestions (flavor_id, suggestion) VALUES (?, ?)"
    params = (flavor_id, suggestion)
    execute_query(query, params)

    print("Suggestion added successfully.")

def add_allergy_concern():
    concern = input("Enter the allergy concern: ")

    query = "INSERT INTO allergy_concerns (concern) VALUES (?)"
    params = (concern,)
    execute_query(query, params)

    print("Allergy concern added successfully.")

def manage_cart(cart):
    while True:
        print("1. View Favorites")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Clear cart")
        print("6. Go back")
        choice = input("Enter your choice: ")

        if choice == '1':
            cart.view_favorites()
        elif choice == '2':
            item = input("Enter item name to add: ")
            cart.add_item(item)
        elif choice == '3':
            item = input("Enter item name to remove: ")
            cart.remove_item(item)
        elif choice == '4':
            cart.view_cart()
        elif choice == '5':
            cart.clear_cart()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    cart = Cart()
    main_menu(cart)
