arr=[10,20,30,40]
pos=int(input("pos = "))
n=len(arr)
arr.append(0)
for i in range(n,pos-1,-1):
    arr[i]=arr[i-1]
arr[pos-1]=int(input("e ="))
print(arr)

#using built in method
arr.insert(2,3000)
print(arr)