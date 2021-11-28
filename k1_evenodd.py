# ----Even and odd -------------min 1:45'

adad = int( input ('Enter a number: '))
if adad < 10: 
    print('E1') if adad %2 == 0 else print ("O1")
elif adad>=9 and adad <100:
    print('E2') if adad %2 == 0 else print ("O2")
else: 
    print('E3') if adad %2 == 0 else print ("O3")
