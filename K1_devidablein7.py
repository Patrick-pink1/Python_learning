#-------------devidable in 7 between 44 and 1089-----min 2:22':35"-------

sum1 = count = 0
for i in range (44,1090):
    if i%7==0:
        count += 1
        sum1 += i
print ( 'Devidable numbers in 7 in range of 44 and 1089 are: %s \n and the sum is %s' %(count,sum1))
