#---average of a list of scores with comma, with function-----min 2:30:45"---

def func1(list_numbers):
      sum1 = count = 0
      for num in list_numbers:
            sum1 += num
            count += 1
      print ("Average is %s" %(sum1/count))
      print('Average: ', sum(list_numbers)/len(list_numbers))

print("----------------------------------------------------")
scores_list = list( map (int , input("Enter numbers with \",\":").split(',')))
func1(scores_list)