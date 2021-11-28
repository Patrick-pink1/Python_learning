def func_ave(scores):
    ave_list = []
    for i in scores:
        ave1= sum(i)/len(i)
        ave_list.append(ave1)
    return(ave_list)

# ---------------------------------------------------------------
numbers = int(input("Enter how many students: "))
score_list = []
for i in range(numbers):
    list1 = list(map(int,input("Enter the numbers: with comma of student {0}: ".format(i+1)).split(",")))
    print(list1)
    score_list.append(list1)
    print(score_list)
print("Average list is: ",func_ave(score_list))
