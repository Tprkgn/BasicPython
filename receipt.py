def main():
    subtotal=38+40+30
    tax=subtotal*0.08
    tip=subtotal*0.15
    total=subtotal+tax+tip
    print("Subtotal: "+str(subtotal))     
    print("Tax: "+str(tax))                  
    print("Tip: "+str(tip))
    print("Total: "+str(total))

main()