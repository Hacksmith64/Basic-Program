def Sort(List):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if List[j] < List[minpos]:
                minpos = j
        temp = List[i]
        List[i] = List[minpos]
        List[minpos] = temp
        print(List)  #Describing Process

List = [5,3,8,6,7,2]
Sort(List)
print(List)

