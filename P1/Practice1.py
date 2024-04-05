name = input("Please enter your name: ")
amount = float(input("Please enter your purchase amount: $"))

tax = (amount * 0.10)

total = amount + tax

print(f"Hello {name}, here is your sales receipt:")
print(f"Subtotal = $ {amount:.2f}")
print(f"     Tax = $ {tax:.2f}")
print(f"             --------")
print(f"   Total = $ {total:.2f}")
