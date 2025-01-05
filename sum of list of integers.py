
list1=input("enter the list of integers seperated by commas")
list1=[int(x) for x in list1.split(',')]
print(list1)
sum=sum(list1)
print(sum)