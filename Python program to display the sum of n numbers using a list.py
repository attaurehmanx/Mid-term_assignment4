
q=[]
size=int(input("enter list num :"))
for i in range(size):
    n = int(input("Enter the value : "))
    q.append(n)
sum=0
for i in range(size):
    sum=sum+q[i]
print("sum of list num=",sum)