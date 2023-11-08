products = [
    {"name": "Smartphone", "price": 500,
     "description": "A handheld device used for communication and browsing the internet."},
    {"name": "Laptop", "price": 1000, "description": "A portable computer that is easy to carry around."},
    {"name": "Headphones", "price": 50, "description": "A pair of earphones worn over the head to listen to music."},
    {"name": "Smartwatch", "price": 300,
     "description": "A wearable device used for fitness tracking and receiving notifications."},
    {"name": "Bluetooth speaker", "price": 100,
     "description": "A portable speaker that connects wirelessly to devices using Bluetooth technology."}
]
cart = []

while True:
    choice = input("Do you want to continue shopping?")
    print (choice)
    if choice == 'y':
        print('Here is a list of products and their prices')
        for index, product in enumerate(products):
            print(f"{index}: {product['name']} : {product['description']} : ${product['price']}")
        product_id = int(input("Enter the id of the product you want to add to the cart"))

        # Check if the product is already present in the cart
        if products[product_id] in cart:
            # If present, increase the quantity of the product
            products[product_id]["quantity"] += 1
        else:
            # If not present, add the product to the cart with a quantity of 1
            products[product_id]["quantity"] = 1
            cart.append(products[product_id])

        # Code to display the current cart contents, including the name, description, price, and quantity
        total = 0
        print('Here are the contents in your cart')
        for product in cart:
            print(f"{product['name']} : {product['description']} : ${product['price']} : QTY:{product['quantity']}")
            total += product['price'] * product['quantity']
        print(f"Cart total is: ${total}")
    else:
        break

print(f"Thank you, your final cart contents are {cart}")