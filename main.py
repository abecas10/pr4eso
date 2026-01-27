'''
This is a simple program that allows you to buy products and find similar products based on tags.

Tags are used to categorize products. For example, a product tagged as "fruit" and "healthy" is a fruit that is healthy.

The program allows you to buy a product and find similar products based on tags.

It is a simple implementation of a recommendation system.

This program is made by: Alex Castella & Gabriel Cereto
'''


products = {
    "Apple": ["fruit", "food", "healthy", "grocery"],
    "Banana": ["fruit", "food", "healthy", "grocery"],
    "Orange": ["fruit", "food", "healthy", "grocery"],
    "Computer": ["electronics", "technology", "pc"],
    "Laptop": ["electronics", "technology", "pc"],
    "Smartphone": ["electronics", "technology", "phone"],
    "Smartwatch": ["electronics", "technology", "watch", "phone"],
    "Weight": ["healthy", "fitness", "gym", "sports"],
    "BotleWater": ["healthy", "fitness", "gym", "sports", "drink"],
    "Coffee": ["food", "grocery", "coffee", "drink"],
    "Milk": ["food", "grocery", "coffee", "drink", "healthy"],
    "Tea": ["food", "grocery", "coffee"],
    "Cookies": ["food", "grocery", "coffee", "snack", "sweet"],
    "Chocolate": ["food", "grocery", "snack", "sweet"],
    "Candy": ["food", "grocery", "snack", "sweet"],
    "Camera": ["electronics", "technology", "camera"],
    "Headphones": ["electronics", "technology", "phone", "watch"],
    "PhoneCase": ["electronics", "technology", "phone"],
    "ScreenProtector": ["electronics", "technology", "phone"],
    "Mouse": ["electronics", "technology", "pc"],
    "Keyboard": ["electronics", "technology", "pc"],
    "Monitor": ["electronics", "technology", "pc", "gaming"],
    "Printer": ["electronics", "technology", "pc"],
    "Console": ["electronics", "technology", "gaming"],
    "GameController": ["electronics", "technology", "gaming"],
    "Tv": ["electronics", "technology", "gaming", "tv"],
    "Batteries": ["electronics", "technology", "tv"],
    "BasketBall": ["sports", "fitness", "basketball"],
    "Football": ["sports", "fitness", "football"],
    "EnergyDrink": ["sports", "fitness", "gym", "drink"],
    "Baseball": ["sports", "fitness", "baseball"],
    "TennisRacket": ["sports", "fitness", "tennis"],
    "Tennisball": ["sports", "fitness", "tennis"],
    "Basketball_Shoes": ["sports", "fitness", "basketball"],
    "Basketball_Shirt": ["sports", "fitness", "basketball"],
    "Football_Shoes": ["sports", "fitness", "football"],
    "Football_Shirt": ["sports", "fitness", "football"],
    "Energybar": ["sports", "fitness", "gym"],
    "Baseball_bat": ["sports", "fitness", "baseball"],
    "Baseball_cap": ["sports", "fitness", "baseball"],
    "Baseball_glove": ["sports", "fitness", "baseball"],
    "Baseball_shirt": ["sports", "fitness", "baseball"],
    "Dog_Food": ["pet", "dog", "food", "grocery"],
    "Dog_champoo": ["pet", "dog", "grocery"],
    "Dog_toy": ["pet", "dog", "toy", "grocery"],
    "Cat_Food": ["pet", "cat", "food", "grocery"],
    "Cat_toy": ["pet", "cat", "toy", "grocery"],
    "Beer": ["food", "grocery", "drink", "alcohol"],
    "Wine": ["food", "grocery", "drink", "alcohol"],
    "Popcorn": ["food", "grocery", "snack", "salty", "tv"],
    "Soda": ["food", "grocery", "drink", "tv"],
    "Juice": ["food", "grocery", "drink", "healthy"],
    "Eggs": ["food", "grocery", "healthy"],
    "Tomato": ["food", "grocery", "healthy"]
}

print(len(products))

buy = input("Buy a product: ")

print("--------------")

if buy in products:
    print(f"Tags: {products[buy]}")
else:
    print("Error: Product not found")

print("--------------")
print("Finding similar products...")

similar_products = []