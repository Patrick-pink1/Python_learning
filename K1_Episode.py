#---------min 3:10:00---------break and continue and flag-------

s = int(input ('Enter series numbers: '))
e = int(input ("Enter episode numbers: "))
flag = False
for i_s in range(1,s+1):
    if flag:
        break
    for i_e in range ( 1,e+1):
        # if i_s ==4:
            # continue
        if i_e ==3:
            break
        if i_s == 4 and i_e == 2:
           flag = True
           break
        print ("S{}E{}".format(i_s,i_e))
# continue: if i_s==4 then the process jump of the 4 and goes to 5
