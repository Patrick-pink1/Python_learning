#numbers of 3digit numbers devidable to 3 and the sum of them

sum1 = sum2  = 0
count1 = count2 = 0
num = 100

while num < 1000:
    if num % 3 ==0:
        count1 += 1
        sum1 += num
        num +=1
    else:
        count2 += 1
        sum2 += num
        num += 1

print (' Devidable are %s and sum of them is %s'%(count1,sum1))
print (' Undevidable are %s and sum of them is %s'%(count2,sum2))

print (' \nDevidable are {0} and sum of them is {1}'.format(count1,sum1))
print ('Undevidable are {0} and sum of them is {1}'.format(count2,sum2))

print (' \nDevidable are ',count1, 'and sum of them is ',sum1)
