class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item(name={self.name}, quantity={self.quantity})"

class Inventory:
    def __init__(self):
        self.items = []

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

def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Items")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            inventory.remove_item(name, quantity)
        elif choice == '3':
            inventory.display_items()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
