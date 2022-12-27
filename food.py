from msilib.schema import SelfReg
from tkinter import Menu, Menubutton
import random
import datetime

class Restaurant:
    
    def __init__(self, name):
        self.restro_name=name
        self.food={}
        self.food_ID=len(self.food)+1
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]

        
    # admin functionalities
    
    
    def admin_register(self):
        try:
            self.admin_email=input("Enter your email id : ")
            self.admin_pass=input("Enter your password : ")
            self.admin_details={"Email_ID":self.admin_email,"Password":self.admin_pass}
            print("\n!! Admin Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restro_name} Restaurant\n")
            print("Admin Details : ")
            for i in self.admin_details:
                print(i, ":", self.admin_details[i])
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")
            
            
    def admin_login(self):
        try:
            print(f"Welcome TO {self.restro_name} Restaurant\n\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.admin_details.values())!=0:
                if email==self.admin_email and pas==self.admin_pass:
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Add Food Item \n2. Edit Food Item\n3. View Food Item\n4. Delete Food Item\n5. Exit")
                        z=input()
                        if z=="1":
                            self.add_food_item()
                        elif z=="2":
                            self.edit_food_item()
                        elif z=="3":
                            self.view_food_item()
                        elif z=="4":
                            self.delete_food_item()
                        elif z=="5":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no Admin Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")
            
        
    def add_food_item(self):
        try:
            name=input("Enter the food name : ")
            quantity=float(input("Enter the quantity in values only : "))
            price=float(input("Enter the price in Rs only : "))
            discount=float(input("Enter the discount in Rs only : "))
            stock=float(input("Enter the available stock in values only : "))
            food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            print("\n!! Food Item added successfully !!\n")
            print("Newly Added items :", self.food,"\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
        
        
    def edit_food_item(self):
        try:
            x=int(input("Enter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \n")
                y= input("Enter the number only : ")
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n!! Successfully Updated !!\n")
                elif y=="2":
                    self.food[x]["Quantity"]=float(input("Updated Quantity in values only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="3":
                    self.food[x]["Price"]=float(input("Updated Price in Rs only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="4":
                    self.food[x]["Discount"]=float(input("Updated Discount in Rs only : "))
                    print("\n!! successfully Updated !!\n")
                elif y=="5":
                    self.food[x]["Stock"]=float(input("Updated Stock in values only : "))
                    print("\n!! Successfully Updated !!\n")
                else:
                    print("!! Sorry Invalid Number !!\n")
            else:
                print("\n!! Incorrect Food ID !!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")  
            
            
    def view_food_item(self):
        print("List of Food Items : \n")
        if len(self.food)!=0:    
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("!! Sorry No Food Items is Added !!\n")
            

    def delete_food_item(self):
        try:
            print("!! Warning !!\nFood Item will Delete Permanently\n")
            print("Enter the Food ID ")
            x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n",self.food)
            else:
                print("!! Incorrect Food ID!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
                
                
    # user functionalities
                   
        
    def user_register(self):
        try:
            user_name=input("Enter your full name : ")
            phone_no=int(input("Enter your 10 digit phone number : "))
            email=input("Enter your email id : ")
            password=input("Enter your password : ")
            address=input("Enter your address with area PIN code ")
            self.user_details={"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
            print("\n!! Your Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restro_name} Restaurant\n")
            print("User Details : ")
            for i in self.user_details:
                print(i, ":", self.user_details[i])        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")      
            
               
    def user_login(self):
        try:
            print(f"Welcome TO {self.restro_name} Restaurant\n\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.user_details.values())!=0:                                                            #we can same as admin by using self.email..etc
                if email==self.user_details["Email_ID"] and pas==self.user_details["Password"]:      # we can make it either object level or local level inside def fun
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit")
                        z=input()
                        if z=="1":
                            self.place_order()
                        elif z=="2":
                            self.ordered_history()
                        elif z=="3":
                            self.update_details()
                        elif z=="4":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no User Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")  
            
            
def place_order(self):
        try:
            if len(self.food)!=0:
                print("list of Availabe Food Items :\n")
                menu=[]
                for items in self.food:
                    menu.append([self.food[items],["1"],["Truffle Cake"], self.food[items]["quantity,500gm"],self.food[items]["price,INR 900"]]) 
                    menu.append([self.food[items],["2"]["Vegan Burger"], self.food[items]["quantity,1 piece"],self.food[items]["price,INR 320"]]) 
                    menu.append([self.food[items],["3"],["Tandoori Chicken"], self.food[items]["quantity,4 pieces"],self.food[items]["price,INR 240"]]) 
                for i in range(len(menu)):
                    print(i+1,".",menu[i])
                while True:
                    print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                    x=input()
                    if x=="1":
                        print("Truffle cake", "quantity,500gm","price,INR900")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-1])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                                print("\nList of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x=="2":
                        print("Vegan Burger", "quantity,1 piece","price,INR320")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-2])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                                print("\nList of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x=="3":
                         print("Tandoori chicken", "quantity,4 piece","price,INR240")
                         y=input().split(",")
                         for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-3])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                                print("\nList of food item you selected : \n")
                         for j in self.ordered_item:
                            print(j)
                    elif x=="4":
                         break
                    else:
                        print("!! Invalid Number !!\n")
            
                        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")     
                
                
    
            
       # defining the Main function    

try:
    def main():
        obj=Restaurant("taj")
        print(f"!!  Welcome To {obj.restro_name} Restaurant  !!\n")
       
        
        while True:
            print("1. Admin\n2. User\n3. Exit\n")
            x=input()
            if x=="1":
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.admin_register()
                    elif y=="2":
                        obj.admin_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")
                    
            elif x=="2":
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.user_register()
                    elif y=="2":
                        obj.user_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")        
            elif x=="3":
                break
            else:
                print("Invalid Number")
except Exception as e:
    print("Something went wrong please give input carefully")
            
        
        # calling the main function 
        
if __name__=='__main__':
    main()


print("THANK YOU SIR")

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

