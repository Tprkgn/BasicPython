def main():
    print("This program converts feet and inches to centimeters.")
    feet = float(input("Enter number of feet: "))
    inch = float(input("Enter number of inches: "))
    cm = (feet*30.48)+(inch*2.54)
    print(str(int(feet))+" ft "+str(int(inch))+" in = "+str(cm)+" cm")
main()