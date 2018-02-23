try:
    total = float(input("Please enter your total: "))

    totalA = format((round((1.15 * total), 2)), ".2f")
    totalB = format((round((1.20 * total), 2)), ".2f")

    print("Your total with a 15% percent tip is $" + str(totalA))
    print("Your total with a 20% percent tip is $" + str(totalB))
    
except ValueError:
    print("That is not a valid number")



