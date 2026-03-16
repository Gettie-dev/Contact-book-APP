foods=[]
prices=[]
total= 0

while True:
    food=input("Enter food name or q to close: ")
    

    if food.lower() =="q":
        break
    else:
        price=float(input(f"Enter price of {foods}:R "))
        foods.append(food)
        prices.append(price)

print("-------YOuR CART-------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print("/n")

print(f"ur total is: R{total}")