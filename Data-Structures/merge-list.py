
#merge two list
def merge(lst1,lst2):
    idx1=0
    idx2=0

    result = []
    while idx1<len(lst1) and idx2 < len(lst2):
        if lst1[idx1] < lst2[idx2]:
            result.append(lst1[idx1])
            idx1 = idx1 + 1
        else:
            result.append(lst2[idx2])
            idx2 = idx2 + 1

    while idx1 < len(lst1):
        result.append(lst[idx1])
        idx1 = idx1 + 1

    while idx2 < len(lst2):
        result.append(lst2[idx2])
        idx2 = idx2 + 1


    return result


print(merge([1,4,6],[2,3,8,9]))

