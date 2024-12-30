n=int(input("Enter the number of name : "))
list = []
count=0
for i in range(n):
    name = input("Enter name : ")
    list.append(name)
for i in list:
    for j in i:
        if(j=="a"):
            count=count+1;
if count==0:
    print("'a' not found")
else:
    print("number of 'a' are",count)
