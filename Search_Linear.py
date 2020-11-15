pos = -1
def Search(arr,n):
    i = 0
    while i < len(arr):
        if arr[i] == n:
            globals()['pos'] = i
            print("Found Here")
            return True
        i = i+1
    return False

arr = [5,8,4,6,9,2]
n = 9
if Search(arr,n):
    print("Found",pos+1)
else:
    print("not Found")
