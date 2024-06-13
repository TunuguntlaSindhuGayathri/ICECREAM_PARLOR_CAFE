class Cart:
    def __init__(self):
        self.items = []
        self.favorites = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from cart.")
        else:
            print(f"{item} is not in the cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Cart items:")
            for item in self.items:
                print(item)

    def clear_cart(self):
        self.items.clear()
        print("Cart has been cleared.")

    def add_favorite(self, item):
            self.favorites.append(item)
            
    def remove_favorite(self, item):
        if item in self.favorites:
            self.favorites.remove(item)
            print(f"Removed {item} from favorites.")
        else:
            print(f"{item} is not in the favorites.")

    def view_favorites(self):
        if not self.favorites:
            print("Favorites list is empty.")
        else:
            print("Favorite items:")
            for item in self.favorites:
                print(item)

    def clear_favorites(self):
        self.favorites.clear()
        print("Favorites list has been cleared.")
