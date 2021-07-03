def merge_sort(arr):
   # comp=lambda x,y: x < y
  #  left = []
   # right = []
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = [i for i in arr[:] if i <= arr[mid] ] 
        right = [i for i in arr[:] if i> arr[mid] ]
#         for i in range(len(arr)):
#             if arr[i] < arr[mid]:
#                 left.append(arr[i])
#             elif arr[i] >= arr[mid]:
#                 right.append(arr[i])
        return merge_sort(left) + [arr[mid]] +merge_sort(right)
a = [3,6,8,9,1,10,7,4,7]
merge_sort(a)