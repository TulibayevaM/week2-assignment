print("Pet Grooming Service Calculator")

total = 0

while True:
    service = input("Enter service (bath, trim, full or done): ")

    if service == "done":
        break

    if service == "bath":
        price = 15
    elif service == "trim":
        price = 25
    elif service == "full":
        price = 40
    else:
        print("Wrong service!")
        continue

    print("Price: $", price)

    total = total + price

    print("Current total: $", total)

discount = 0

if total >= 75:
    discount = 12

final_total = total - discount

print("----- Final Receipt -----")
print("Subtotal: $", total)
print("Discount: $", discount)
print("Final total: $", final_total)
print("Thank you!")

