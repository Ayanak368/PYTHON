list = []
sum = 0
limit = int(input("Enter the limit: "))
print("Enter", limit, "numbers: ")
for i in range(limit):
    num = int(input())
    list.append(num)
print(list)
for i in list:
    sum = sum + i
print("Sum of list: ", sum)