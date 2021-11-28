# Test for to find an input name in another inpt names list, 1:35':10"

string = input ( "Enter some names by space distance: ")
name = input ("Enter your name your are searching: ")

list1 = string.split()

# if name in list1:
#     print ('YES')
# else:
#      print ('NO')

print ('Yes') if name in list1 else print("No")
