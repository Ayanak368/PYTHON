data=input("enter list of integer separated by space:")
list=data.split()
listout=[]
for x in list:
    x=int(x)
    if x>100:
        listout.append("over")
    else:
        listout.append("x")
print(listout)
