arr = [1, 2, 3, 4]
print(len(arr))

element = int(input("Enter the element at index 0: "))

arr.append(0)   # increase list size by 1

for i in range(len(arr)-2, -1, -1):   # start from last valid index
    arr[i+1] = arr[i]

arr[0] = element

print(arr)


#using built in method
# Python program to insert a given element at the beginning 
# of an array

arr = [10, 20, 30, 40]
element = 50
print("Array before insertion")
for i in range(len(arr)):
	print(arr[i], end=" ")

# Insert element at the beginning
arr.insert(0, element)

print("\nArray after insertion")
for i in range(len(arr)):
    print(arr[i], end=" ")