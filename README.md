# ICE CREAM PARLOR CAFE APPLICATION

Welocome to Ice Cream Parlor Cafe command-line Application. This allows users to interact with seasonal flavor offerings, check ingredient inventory, add customer flavor suggestions, customer allergy concerns, and manage cart.

## Prerequisites

Make sure you have installed :
*python (version 3.x.x)
*SQLite

## Installation Steps:

1.Clone repository
->git clone <repository-url>
->cd <repository-folder>

2.Setup the database
create a new SQLite database file named "icecream_parlor_cafe.db"
->sqlite3 icecream_parlor_cafe.db
(or)
to initialize the database schema and insert initial data(make sure you have the initialize_db.py file in the project directory)
->python3 initialize_db.py

3.Dependencies
If you are using mac no dependencies needed
For windows - make sure you have the requirements.txt file in the project directory which contains all necessary dependencies.
->pip install -r requirements.txt

## Running the Application

To start the application run the following command:
->python3 app.py("MacOS")
->python app.py("Windows")

## Notes

->View and Search Seasonal Flavor Offerings:
Search for specific flavors or view all available seasonal offerings.
->View Ingredient Inventory:
Check the current stock of ingredients.
->Add Customer Flavor Suggestion:
Submit new flavor suggestions.
->Add Allergy Concern:
Record allergy concerns for customer safety.
->Manage Cart:
Add items to the cart, view favorites, and manage cart items like clear cart, view cart, remove item from cart.

## Additional Information

->Database: The SQLite database (icecream_parlor_cafe.db) stores all application data.
->Files:
main.py: It imports and runs the main_menu function from the app module.
app.py: Main application script.
cart.py, database.py, models.py, utils.py: Modules for different aspects of the application (cart management, database operations, data models, utility functions).

## Documentation of test steps

Welcome to the Ice Cream Parlor Cafe

1. View and Search Seasonal Flavor Offerings
2. View Ingredient Inventory
3. Add Customer Flavor Suggestion
4. Add Allergy Concern
5. Manage Cart
6. Exit
   Enter your choice: 1
   Enter flavor to search for (leave blank to view all):
   ID: 1, Name: Vanilla, Seasonal: 1
   ID: 2, Name: Chocolate, Seasonal: 0
   ID: 3, Name: Strawberry, Seasonal: 1
   Select an action:
7. Add to cart
8. Add to favorites
   Enter your choice: 2
   Enter the ID of the flavor to add to favorites: 3
   Strawberry added to favorites.
9. View and Search Seasonal Flavor Offerings
10. View Ingredient Inventory
11. Add Customer Flavor Suggestion
12. Add Allergy Concern
13. Manage Cart
14. Exit
    Enter your choice: 1
    Enter flavor to search for (leave blank to view all):
    ID: 1, Name: Vanilla, Seasonal: 1
    ID: 2, Name: Chocolate, Seasonal: 0
    ID: 3, Name: Strawberry, Seasonal: 1
    Select an action:
15. Add to cart
16. Add to favorites
    Enter your choice: 1
    Enter the ID of the flavor to add to cart: 2
    Chocolate added to cart.
17. View and Search Seasonal Flavor Offerings
18. View Ingredient Inventory
19. Add Customer Flavor Suggestion
20. Add Allergy Concern
21. Manage Cart
22. Exit
    Enter your choice: 2
    ID: 1, Name: Milk, Quantity: 20
    ID: 2, Name: Sugar, Quantity: 15
    ID: 3, Name: Vanilla Extract, Quantity: 5
23. View and Search Seasonal Flavor Offerings
24. View Ingredient Inventory
25. Add Customer Flavor Suggestion
26. Add Allergy Concern
27. Manage Cart
28. Exit
    Enter your choice: 5
29. View Favorites
30. Add item to cart
31. Remove item from cart
32. View cart
33. Clear cart
34. Go back
    Enter your choice: 1
    Favorite items:
    Strawberry
35. View Favorites
36. Add item to cart
37. Remove item from cart
38. View cart
39. Clear cart
40. Go back
    Enter your choice: 6
41. View and Search Seasonal Flavor Offerings
42. View Ingredient Inventory
43. Add Customer Flavor Suggestion
44. Add Allergy Concern
45. Manage Cart
46. Exit
    Enter your choice: 6
    Thank you for visiting the Ice Cream Parlor Cafe!

## SQL Query or ORM abstraction Implementation

1.Create Tables and Insert Initial Data
2.Fetching Seasonal Flavor Offerings
3.Adding Customer Flavor Suggestion

## Docker File

1. **Clone the repository**

   ```sh
   git clone <repository-url>
   cd ice-cream-parlor-cafe
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Initialize the database**

   ```sh
   python initialize_db.py
   ```

5. **Run the main application**

   ```sh
   python app.py
   ```
