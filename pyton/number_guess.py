## choose the number
import numpy as np
print("choose any number between 1 to 60\n")
print("check your digit in the following matrix\n ")
arr1 = np.array([[1,3,5,7,9],[11,13,15,17,19],[21,23,25,27,29],[31,33,35,37,39],[41,43,45,47,49],[51,53,55,57,59]])
res = 0
print(arr1)
key = input("press 'y' if present\n press 'n' if not present\n")
if key == 'y':
    res += arr1[0,0]
else:
    res += 0

arr2 = np.array([[2,3,6,7,10],[11,14,15,18,19],[22,23,26,27,30],[31,34,35,38,39],[42,43,46,47,50],[51,54,55,58,59]])

print(arr2)
key = input("press 'y' if present\n press 'n' if not present\n")
if key == 'y':
    res += arr2[0,0]
else:
    res += 0

arr3 = np.array([[4,5,6,7,11],[12,13,14,15,20],[21,22,23,28,29],[30,31,36,37,38],[39,44,45,46,47],[52,53,55,60,' ']])
print(arr3)
key = input("press 'y' if present\n press 'n' if not present\n")
if key == 'y':
    res += int(arr3[0,0])
else:
    res += 0

arr4 = np.array([[8,9,10,11,12],[13,14,15,24,25],[26,27,28,29,30],[31,40,41,42,43],[44,45,46,47,56],[57,58,59,60,' ']])
print(arr4)
key = input("press 'y' if present\n press 'n' if not present\n")
if key == 'y':
    res += int(arr4[0,0])
else:
    res += 0

arr5 = np.array([[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30],[31,48,49,50,51],[52,53,54,55,56],[57,58,59,60,' ']])
print(arr5)
key = input("press 'y' if present\n press 'n' if not present\n")
if key == 'y':
    res += int(arr5[0,0])
else:
    res += 0

arr6 = np.array([[32,33,34,35,36],[37,38,39,40,41],[42,43,44,45,46],[47,48,49,50,51],[52,53,54,55,56],[57,58,59,60,' ']])
print(arr6)
key = input("press 'y' if present\n press 'n' if not present\n")
if key == 'y':
    res += int(arr6[0,0])
else:
    res += 0


print("\nyour choosen number is : ", res)
