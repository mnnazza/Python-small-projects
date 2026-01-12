foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or q to quit: ")
    if food == "q":
        break
    else:

        price = float(input("Enter the price of the food item: "))
        foods.append(food)
        prices.append(price)

        print("----YOUR CART----")

    for food in foods:
        print(food, end=" ")

        print()

    for price in prices:
        total = total + price

    print(f"Your total is ${total}")
