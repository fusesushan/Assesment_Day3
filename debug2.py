class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_to_menu(self, food_item, quantity):
        if food_item in self.menu:
            self.menu[food_item] += quantity
        else:
            self.menu[food_item] = quantity

    def remove_from_menu(self, food_item, quantity):
        if food_item in self.menu:
            if self.menu[food_item] <= quantity:
                del self.menu[food_item]
            else:
                self.menu[food_item] -= quantity
        else:
            print(f"{food_item.name} not found in the menu.")

    def get_total_revenue(self):
        total_revenue = 0
        for food_item, quantity in self.menu.items():
            total_revenue += food_item.price * quantity
        return total_revenue

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cart = {}

    def add_to_cart(self, food_item, quantity):
        if quantity > 0:
            if food_item in self.cart:
                self.cart[food_item] += quantity
            else:
                self.cart[food_item] = quantity
        else:
            print("Quantity must be greater than zero.")

    def remove_from_cart(self, food_item, quantity):
        if food_item in self.cart:
            if self.cart[food_item] <= quantity:
                del self.cart[food_item]
            else:
                self.cart[food_item] -= quantity
        else:
            print(f"{food_item.name} not found in the cart.")

class DeliveryService:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def find_restaurant_by_name(self, name):
        for restaurant in self.restaurants:
            if restaurant.name == name:
                return restaurant
        return None

# Test the food delivery system
restaurant1 = Restaurant("My Resturant1")
restaurant2 = Restaurant("My Resturant2")

food_item1 = FoodItem("MoMo", 150)
food_item2 = FoodItem("Chowmein", 180)
food_item3 = FoodItem("Tea", 25)

restaurant1.add_to_menu(food_item1, 5)
restaurant1.add_to_menu(food_item2, 3)

restaurant2.add_to_menu(food_item2, 2)
restaurant2.add_to_menu(food_item3, 2)

customer = Customer("Sushan", "333, street S.")
customer.add_to_cart(food_item1, 2)
customer.add_to_cart(food_item2, 3)
customer.add_to_cart(food_item3, -1)  # Bug: This should print an error message

delivery_service = DeliveryService()
delivery_service.add_restaurant(restaurant1)
delivery_service.add_restaurant(restaurant2)

restaurant1.remove_from_menu(food_item2, 5)  # Bug: This should print an error message

restaurant2.remove_from_menu(food_item1, 1)  # Bug: This should print an error message

print("Total revenue for My Resturant1:", restaurant1.get_total_revenue())
print("Total revenue for My Resturant2:", restaurant2.get_total_revenue())
