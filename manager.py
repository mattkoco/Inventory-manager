import json
import hashlib

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item(name={self.name}, quantity={self.quantity})"

    def to_dict(self):
        return {'name': self.name, 'quantity': self.quantity}

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

class Inventory:
    def __init__(self):
        self.items = []
        self.users = []

    def add_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return
        new_item = Item(name, quantity)
        self.items.append(new_item)

    def remove_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                else:
                    print(f"Cannot remove {quantity} {name}(s). Only {item.quantity} available.")
                if item.quantity == 0:
                    self.items.remove(item)
                return
        print(f"Item {name} not found in inventory.")

    def display_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items:
                print(item)

    def search_item(self, name):
        for item in self.items:
            if item.name == name:
                print(item)
                return
        print(f"Item {name} not found in inventory.")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([item.to_dict() for item in self.items], f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                items = json.load(f)
                self.items = [Item(item['name'], item['quantity']) for item in items]
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def add_user(self, username, password):
        for user in self.users:
            if user.username == username:
                print("Username already exists.")
                return
        new_user = User(username, password)
        self.users.append(new_user)

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == hashlib.sha256(password.encode()).hexdigest():
                print("Authentication successful.")
                return True
        print("Authentication failed.")
        return False

def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            inventory.add_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if inventory.authenticate_user(username, password):
                while True:
                    print("\nUser Menu")
                    print("1. Add Item")
                    print("2. Remove Item")
                    print("3. Display Items")
                    print("4. Search Item")
                    print("5. Save Inventory to File")
                    print("6. Load Inventory from File")
                    print("7. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        name = input("Enter item name: ")
                        quantity = int(input("Enter item quantity: "))
                        inventory.add_item(name, quantity)
                    elif user_choice == '2':
                        name = input("Enter item name: ")
                        quantity = int(input("Enter item quantity: "))
                        inventory.remove_item(name, quantity)
                    elif user_choice == '3':
                        inventory.display_items()
                    elif user_choice == '4':
                        name = input("Enter item name: ")
                        inventory.search_item(name)
                    elif user_choice == '5':
                        filename = input("Enter filename: ")
                        inventory.save_to_file(filename)
                    elif user_choice == '6':
                        filename = input("Enter filename: ")
                        inventory.load_from_file(filename)
                    elif user_choice == '7':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
