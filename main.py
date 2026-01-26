

class product:
    def __init__(self,name,price,quantity, tags):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.tags = tags

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Tags: {', '.join(self.tags)}")


print("-------------------------")

Apple = product("Apple", 0.99, 100, ["fruit", "food", "healthy", "grocery"])
Apple.display_info()

print("-------------------------")

Banana = product("Banana", 0.99, 100, ["fruit", "food", "healthy", "grocery"])
Banana.display_info()

print("-------------------------")

Orange = product("Orange", 0.99, 100, ["fruit", "food", "healthy", "grocery"])
Orange.display_info()

print("-------------------------")

Computer = product("Computer", 999.99, 50, ["electronics", "technology", "pc"])
Computer.display_info()

print("-------------------------")

Laptop = product("Laptop", 999.99, 50, ["electronics", "technology", "pc"])
Laptop.display_info()

print("-------------------------")

Smartphone = product("Smartphone", 999.99, 50, ["electronics", "technology", "phone"])
Smartphone.display_info()

print("-------------------------")

SmartWatch = product("Smartwatch", 999.99, 50, ["electronics", "technology", "watch", "phone"])
SmartWatch.display_info()

print("-------------------------")

Weights = product("Weight", 0.99, 100, ["healthy", "fitness", "gym", "sports"])
Weights.display_info()

print("-------------------------")

BotleWater = product("BotleWater", 0.99, 100, ["healthy", "fitness", "gym", "sports"])
BotleWater.display_info()

print("-------------------------")

Coffee = product("Coffee", 0.99, 100, ["food", "grocery", "coffee"])
Coffee.display_info()

print("-------------------------")

Milk = product("Milk", 0.99, 100, ["food", "grocery", "coffee"])
Milk.display_info()

print("-------------------------")

Tea = product("Tea", 0.99, 100, ["food", "grocery", "coffee"])
Tea.display_info()

print("-------------------------")

Cookies = product("Cookies", 0.99, 100, ["food", "grocery", "coffee", "snack"])
Cookies.display_info()

print("-------------------------")

Chocolate = product("Chocolate", 0.99, 100, ["food", "grocery", "snack"])
Chocolate.display_info()

print("-------------------------")

Candy = product("Candy", 0.99, 100, ["food", "grocery", "snack"])
Candy.display_info()

print("-------------------------")

Camera = product("Camera", 999.99, 50, ["electronics", "technology", "camera"])
Camera.display_info()

print("-------------------------")

Headphones = product("Headphones", 999.99, 50, ["electronics", "technology", "phone", "watch"])
Headphones.display_info()

print("-------------------------")

PhoneCase = product("PhoneCase", 999.99, 50, ["electronics", "technology", "phone"])
PhoneCase.display_info()

print("-------------------------")

ScreenProtector = product("ScreenProtector", 999.99, 50, ["electronics", "technology", "phone"])
ScreenProtector.display_info()

print("-------------------------")

Mouse = product("Mouse", 999.99, 50, ["electronics", "technology", "pc"])
Mouse.display_info()

print("-------------------------")

Keyboard = product("Keyboard", 999.99, 50, ["electronics", "technology", "pc"])
Keyboard.display_info()

print("-------------------------")

Monitor = product("Monitor", 999.99, 50, ["electronics", "technology", "pc"])
Monitor.display_info()

print("-------------------------")