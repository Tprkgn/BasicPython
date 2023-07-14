def main():
    # Calculate total owed, assuming 8% tax / 15% tip
    input1 = input("What was the meal cost?")
    subtotal = int(input1)
    tax = subtotal * .08
    tip = subtotal * .15
    total = subtotal + tax + tip
    
    print("Subtotal: "+ str(subtotal))
    print("Tax: "+ str(tax))
    print("Tip: "+ str(tip))
    print("Total: "+ str(total))

main()