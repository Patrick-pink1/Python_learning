#-----------average of a list of scores with comma-----min 2:30:45"---

scores = input ("Enter your numbers with \",\" between them:")
# scores = input ("Enter your numbers with comma between them:")
print ('type(scores): ',type(scores),scores)
print('scores.split(','): ',scores.split(','))
print('map(int, scores.split(',')): ',map(int, scores.split(',')))
print('list(map(int, scores.split(','))): ',list(map(int, scores.split(','))))

print("----------------------------------------------------")
scores_list = list( map (int , input("Enter numbers with \",\":").split(',')))
print ('scores_list: ',scores_list)
sum1 = count = 0
for score in scores_list:
      sum1 += score
      count += 1
print ("Average is %s" %(sum1/count))
print("Average is sum(scores_list)/len(scores_list) :",sum(scores_list)/len(scores_list))


