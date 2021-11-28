#---average of a list of scores with comma, with function-----min 2:54:00"---

def func_ave(list_numbers):
      sum1 = 0
      for num in list_numbers:
            sum1 += num
      ave_now = sum1 / (len(list_numbers))
      return ave_now
                        
print("----------------------------------------------------")

#scores_list = list( map (int , input("Enter numbers with \",\":").split(',')))
score_list = [ [19,19,18,18],
               [13.14,15.11],
               [6,7,8,9,10] ]
for student in score_list:
      average = func_ave(student)
      print ("type(average): ",type(average))
      print(average, end ="")
      for i in range(int(average)): 
            print ("*",end="")  
      print()

