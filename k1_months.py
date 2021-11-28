 # If user enter the number of month, we say which month is.

# اگر کاربر شماره وارد کند، ما مي گوييم کدام ماه است

list_months = [ 'Jan' , 'Feb' , 'Mars' , 'April' , 'May' , 'June',
                'July' , 'Aug', 'Sep' , 'Oct' , 'Nov' , 'Dec' ]

flag = True
while flag:
    num = int ( input ( 'Enter the number of months (1-12): '))
    if 0 < num <= 12:          
        #you must select (num - 1) whn you call list
        print ( num , 'months of year is' , list_months[num-1])
        print ( '%s months of year is %s' %(num , list_months[num-1]))
        print ( '{0} months of year is {1}'.format(num , list_months[num-1]))
        flag = False
    else:
        print("your number is not 1 to 12, try again")
        

