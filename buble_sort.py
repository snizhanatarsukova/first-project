def bubbleSort(arr):
    n = len(arr)
   
    swapped = False # should be false always
    for i in range(n-1):
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 
arr = [64, 34, 25, 12, 22, 11, 90]
arr = [64, 34, 25, 12, 22, 11, 90]
arr = [64, 34, 25, 12, 22, 11, 90]
arr = [64, 34, 25, 12, 22, 11, 90]
arr = [64, 34, 25, 12, 22, 11, 90]
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
