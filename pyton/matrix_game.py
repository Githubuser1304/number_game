import numpy as np
unique_numbers = np.random.permutation(16)
arr = unique_numbers.reshape((4, 4))

print(arr)

while 1:
    key = int(input("\n\n1. for left\n 2. for down\n 3. for right\n 5. for up \n9. for quit\n" ))
    if key == 1:   # down ka kaam kr rha hai
        x,y = np.where(arr == 0)
        arr[x,y], arr[x,(y+1)%4] = arr[x,(y+1)%4], arr[x,y] #swapping
        print(arr)

    if key == 2:
        x,y = np.where(arr == 0)  #right me ja rha hai
        print(x,y)
        arr[x,y], arr[x-1,y] = arr[x-1,y], arr[x,y] #swapping
        print(arr)

    if key == 3:   # up ke liye kaam kr rhahai
        x,y = np.where(arr == 0)
        arr[x,y], arr[x,y-1] = arr[x,y-1], arr[x,y] #swapping
        print(arr)

    if key == 5:   # left ke liye kaam krrha 
        x,y = np.where(arr == 0)
        arr[x,y], arr[(x+1)%4,y] = arr[(x+1)%4,y], arr[x,y] #swapping
        print(arr)

    if key == 9:
        break
    if key not in (1,2,3,5,9):
        print("\nPlease press correct key\n")