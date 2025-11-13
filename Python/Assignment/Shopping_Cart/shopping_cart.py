class Products:
    def __init__(self, product_id, product_name, product_price, product_quantity):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price
        self.__product_quantity = product_quantity
    
    def __str__(self):
        return f"Product ID: {self.__product_id}, Name: {self.__product_name}, Price: {self.__product_price}, Quantity: {self.__product_quantity}"
    
    @property
    def id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__product_name

    @property
    def price(self):
        return self.__product_price

    @property
    def quantity(self):
        return self.__product_quantity

    def set_quantity(self, quantity):
        self.__product_quantity = quantity


# ------------------------------------- Wallet -------------------------------------
class Wallet:
    def __init__(self, balance=0.0):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance 
    
    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} added to wallet. Current Balance: {self.__balance}\n")
        else:
            print("Invalid amount")

    def deduct_balance(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            print(" empty wallet ")
            return False


# -------------------------------------- Shopping Cart -----------------------------------------
class ShoppingCart:
    def __init__(self):
        self.products = [
            Products(1, "Laptop", 50000, 5),
            Products(2, "Phone", 15000, 10),
            Products(3, "Charger", 2000, 15),
            Products(4, "Headphones", 2500, 8),
            Products(5, "Keyboard", 3000, 6)
        ]
        self.cart = []

    def show_products(self):
        print("\n---  Available Products ---\n")
        for p in self.products:
            print(p)
        print()

    def add_to_cart(self, product_id, quantity):
        for product in self.products:
            if product.id == product_id:
                if quantity <= product.quantity:
                    total_price = product.price * quantity
                    self.cart.append({
                        "id": product.id,
                        "name": product.name,
                        "price": product.price,
                        "quantity": quantity,
                        "total": total_price
                    })
                    product.set_quantity(product.quantity - quantity)
                    print(f" quantity {quantity} name  {product.name} added to cart!\n")
                else:
                    print(" Not enough stock available!\n")
                return
        print(" Invalid product ID\n")
        

    def show_cart(self):
        print("\n---  Your Cart ---")
        if not self.cart:
            print("Cart is empty!\n")
            return

        total = 0
        for item in self.cart:
            print(f"quantity {item['quantity']} name {item['name']} price  {item['price']} total {item['total']}")
            total += item['total']
        print(f"Total: {total}\n")

    def calculate_total(self):
        return sum(item['total'] for item in self.cart)

    def clear_cart(self):
        self.cart = []


# -------------------------------------- Main App -----------------------------------------
if __name__ == "__main__":
    shop = ShoppingCart()
    wallet = Wallet(50000.0)  

    while True:
        print("============== Shopping Cart ==============")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. Show Cart")
        print("4. Add Money to Wallet")
        print("5. Checkout & Pay Bill")
        print("6. Show Wallet Balance")
        print("7. Exit")
        print("==================================")

        try:
            choice = int(input("Select your choice: "))
        except ValueError as e:
            print(e)
            continue

        match choice:
            case 1:
                shop.show_products()

            case 2:
                try:
                    pid = int(input("Enter Product ID: "))
                    qty = int(input("Enter Quantity: "))
                    shop.add_to_cart(pid, qty)
                except ValueError as e:
                    print(e)

            case 3:
                shop.show_cart()

            case 4:
                try:
                    amount = float(input("Enter amount to add: "))
                    wallet.add_balance(amount)
                except ValueError:
                    print("Enter valid amount.\n")

            case 5:
                if not shop.cart:
                    print("Cart is empty\n")
                    continue

                total = shop.calculate_total()
                print(f"Total Bill: {total}")
                confirm = input("Buy Now (y/n): ").lower()

                if confirm == 'y':
                    if wallet.deduct_balance(total):
                        print("Payment successful! Order placed.\n")
                        shop.clear_cart()
                        print(f"Remaining Wallet Balance: {wallet.get_balance()}\n")
                else:
                    print("Checkout cancelled.\n")

            case 6:
                print(f"Wallet Balance: {wallet.get_balance()}\n")

            case 7:
                print("Thank you for shopping")
                break

            case _:
                print("Invalid choice! Please try again.\n")
