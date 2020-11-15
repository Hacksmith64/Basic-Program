pos = -1
def Search(List,n):
    l = 0
    u = len(List)-1
    while l <= u:
        mid = (l+u) // 2
        if List[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if List[mid] < n:
                l =mid + 1
            else:
                u = mid - 1
    return False
List = [4,7,8,12,45,99]
print(List)
n = int(input("Enter the Value"))
if Search(List,n):
    print("Found Here",pos+1)
else:
    print("Not Found")