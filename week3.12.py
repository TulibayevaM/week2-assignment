print("Arcade Game Center Calculator")

total = 0

while True:
    game = input("Enter game type (classic, modern, premium or done): ")

    if game == "done":
        break

    if game == "classic":
        price = 0.50
    elif game == "modern":
        price = 1.50
    elif game == "premium":
        price = 2.50
    else:
        print("Wrong game type!")
        continue

    print("Price: $", price)

    total = total + price

    print("Current total: $", total)

bonus = 0

if total >= 10:
    bonus = 1.50

final_total = total - bonus

print("----- Game Summary -----")
print("Subtotal: $", total)
print("Token Bonus Credit: $", bonus)
print("Final Total: $", final_total)
print("Thank you for playing!")
