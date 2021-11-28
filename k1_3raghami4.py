def func_3raghamni(num):
    count1 = count2 = 0
    sum1 = sum2 = 0
    for i in range( 100,1000):
        if i % 3 == 0 :
            count1 += 1
            sum1 += i
        else:
            count2 += 1
            sum2 += i
    return(count1,count2,sum1,sum2)
# ---------------------------------------------------------------------------------
adad= int(input("Enter your maximum number: "))
print(func_3raghamni(adad))
print("devidable: %s\nSum devidable:%s"%(func_3raghamni(adad)[0],func_3raghamni(adad)[2]))
print("Undevidable: %s\nSum undevidable:%s"%(func_3raghamni(adad)[1],func_3raghamni(adad)[3]))