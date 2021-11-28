
while True:
    adad = int(input("Enter a number: "))
    print("Your number is: %s" %adad)
    if adad <10:
        print("Your number is one digit and Even") if adad%2 == 0 else print("Your number one digit and Odd")
    elif 10<= adad <100:
        print("Your number is two digit and Even") if adad%2 == 0 else print("Your number two digit and is Odd")
    elif 100<= adad <1000:
        print("Your number is three digit and Even") if adad%2 == 0 else print("Your number is three digit Odd")
    elif 1000<= adad <10000:
        print("Your number is four digit and Even") if adad%2 == 0 else print("Your number is four digit and Odd")
    else:
        print("Your number is Even") if adad%2 == 0 else print("Your number is Odd")
        print("end of loop")
        break