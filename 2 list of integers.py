list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8]
print("Elements in list one is: ", list1)
print("Elements in list two is: ", list2)
if len(list1) == len(list2):
    print("Lists have same length")
else:
    print("Lists have different length")


if sum(list1)== sum(list2):
   print("The sum of lists are same")
else:
   print("The sum of lists are different")
print("The common element in list is: ")
for i in list1:
  for j in list2:
     if i == j:
          print(i)