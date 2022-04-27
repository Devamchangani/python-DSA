def inch_TO_cm(inch):
    return(inch * 2.54)

i = int(input("Enter the inch: "))
ic = inch_TO_cm(i)
print(f"Centimeter  is{str(ic)}")