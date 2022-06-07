tax = int(input("Enter your tax in price:"))

if tax > 100000:
    print("15% tax for", tax)
elif tax > 50000 and tax <= 100000:
    print("10% tax for", tax)
elif tax <= 50000:
    print("5% tax for", tax)
