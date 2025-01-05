first = 0
second = 1
limit = int(input("Enter the limit: "))
print("The Fibonacci series up to", limit, "terms are:")
print(first)
print(second)
for i in range(2,limit):
     third = first + second
     first = second
     second = third
     print(third)