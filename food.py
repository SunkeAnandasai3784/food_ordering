import random
import datetime

# Admin class to handle the functionalities for the admin
class Admin:
    def __init__(self):
        # Initialize an empty dictionary to store the food items
        self.food_items = {}

    def add_food_item(self, name, quantity, price, discount, stock):
        # Generate a unique FoodID using random module
        food_id = random.randint(1, 10000)

        # Create a dictionary to store the food item details
        food_item = {
            "food_id": food_id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "discount": discount,
            "stock": stock
        }

        # Add the food item to the food_items dictionary
        self.food_items[food_id] = food_item

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        # Check if the food item exists in the food_items dictionary
        if food_id in self.food_items:
            # Update the food item details
            self.food_items[food_id]["name"] = name
            self.food_items[food_id]["quantity"] = quantity
            self.food_items[food_id]["price"] = price
            self.food_items[food_id]["discount"] = discount
            self.food_items[food_id]["stock"] = stock
        else:
            print(f"Food item with FoodID {food_id} does not exist.")

    def view_food_items(self):
        # Print the food item details for all food items
        for food_id, food_item in self.food_items.items():
            print(f"FoodID: {food_id}")
            print(f"Name: {food_item['name']}")
            print(f"Quantity: {food_item['quantity']}")
            print(f"Price: {food_item['price']}")
            print(f"Discount: {food_item['discount']}")
            print(f"Stock: {food_item['stock']}")
            print()

    def remove_food_item(self, food_id):
        # Check if the food item exists in the food_items dictionary
        if food_id in self.food_items:
            # Remove the food item from the food_items dictionary
            del self.food_items[food_id]
        else:
            print(f"Food item with FoodID {food_id} does not exist.")
# Create an instance of the Admin class
admin = Admin()

# Add a food item
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 10, 20)

# Edit the food item
admin.edit_food_item(1, "Tandoori Chicken", "4 pieces", 250, 15, 25)

# View the list of all food items
admin.view_food_items()


# Remove the food item
admin.remove_food_item(1)

# View the list of all food items
admin.view_food_items()

# Output:
# There are no food items in the menu.

# User class to handle the functionalities for the user
class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

        # Initialize an empty list to store the orders placed by the user
        self.orders = []
    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password


# Create a user object
user = User("John Doe", "1234567890", "john.doe@example.com", "123 Main Street", "password")

# Update the profile details of the user
user.update_profile("Jane Doe", "9876543210", "jane.doe@example.com", "456 Main Street", "new_password")

# Print the updated profile details of the user
print(f"Full Name: {user.full_name}")
print(f"Phone Number: {user.phone_number}")
print(f"Email: {user.email}")
print(f"Address: {user.address}")
print(f"Password: {user.password}")


# Create a user object
user = User("John Doe", "1234567890", "john.doe@example.com", "123 Main Street", "password")

# Create an instance of the Admin class
admin = Admin()

# Add some food items to the menu
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin.add_food_item("Vegan Burger", "1 Piece", 320, 10, 5)
admin.add_food_item("Truffle Cake", "500gm", 900, 20, 2)

# View the list of all food items
print("Menu:")
admin.view_food_items()

# Place a new order
print("Please enter the FoodIDs of the items you want to order:")
food_ids = input()

# Convert the input string to a list of integers
food_ids = [int(x) for x in food_ids.split()]

# Initialize an empty list to store the selected food items
selected_food_items = []

# Loop through the list of FoodIDs and add the corresponding food items to the selected_food_items list
for food_id in food_ids:
    if food_id in admin.food_items:
        selected_food_items.append(admin.food_items[food_id])
    else:
        print(f"Food item with FoodID {food_id} does not exist.")

# Print the selected food items
print("Selected food items:")
for food_item in selected_food_items:
    print(f"{food_item['name']} ({food_item['quantity']}) [INR {food_item['price']}]")

# Place the order
print("Do you want to place the order? (y/n)")
choice = input()

if choice == "y":
    # Calculate the total price of the order
    total_price = sum([food_item['price'] for food_item in selected_food_items])

    # Create a dictionary to store the order details
    order = {
        "order_id": random.randint(1, 10000),
        "food_items": selected_food_items,
        "total_price": total_price,
        "timestamp": datetime.datetime.now()
    }

    # Add the order to the orders list of the user
    user.orders.append(order)

    print("Order placed successfully!")
else:
    print("Order cancelled.")

# View the order history
print("Order history:")
for order in user.orders:
    print(f"Order ID: {order['order_id']}")
    print(f"Food Items: {[food_item['name'] for food_item in order['food_items']]}")
    print(f"Total Price: INR {order['total_price']}")
    print(f"Timestamp: {order['timestamp']}")
    print()

# User class to handle the functionalities for the user
class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
    

        # Initialize an empty list to store the orders placed by the user
        self.orders = []
    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password




# Print the updated profile details of the user
print(f"Full Name: {user.full_name}")
print(f"Phone Number: {user.phone_number}")
print(f"Email: {user.email}")
print(f"Address: {user.address}")
print(f"Password: {user.password}")

# Create a user object
user = User("John Doe", "1234567890", "john.doe@example.com", "123 Main Street", "password")

# Update the profile details of the user
user.update_profile("Jane Doe", "9876543210", "jane.doe@example.com", "456 Main Street", "new_password")

