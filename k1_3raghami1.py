# تعداد اعداد سه رقمي بخش پذير بر عدد سه را محاسبه و نشان دهد

num = 100
sum1 = sum2 =0
count = count1 = 0

# for i in range (100,1000):
while num <1000:
    #list1().append('num')
    if num % 3 == 0:
        sum1 += num
        #print (num)
        count += 1
        num += 1
    else:
        count1 += 1
        num += 1
        sum2 += num
       
print ( 'Numbers are devidable to 3: %s \nNumbers are not devidable to 3 are:%s' %(count , count1))      
print ('Sum of devidable is: {0} \nSum of undevidable is: {1}'.format(sum1,sum2)) 
#print (list1)

