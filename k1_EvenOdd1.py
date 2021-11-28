# پيدا کردن اينکه عددي که کاربر وارد کرده است زوج است يا فرد

while True:
    a = int(input ("Please enter a number: "))
    if a%2 == 0:
        print (" %s is even" %a)
    else:
        print (" %s is odd" %a)
