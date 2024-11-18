from array import *

arr = array('i',[2,4,6,8,10,12])
print (arr)

arr1 = array('f',[2.5,4.5,6.5,8.5,10.5,12.5])
print (arr1)

arr.append(12)
print (arr)

arr.insert(0, 0)
print (arr)

arr.extend([1,3,5,7,9,11])
print(arr)

for i in arr:
     print(i)

print(arr[0])

arr.remove(arr[0])
print(arr)




