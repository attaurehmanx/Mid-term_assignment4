
list=[1,2,3,4,6,7,8,1,2,3,4,5,6,7,]
unique_list=[]
for a in list:
    if a not in unique_list:
        unique_list.append(a)
print(unique_list)