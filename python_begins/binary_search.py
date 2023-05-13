def binearysearch(ar, k):
    s = 0
    e = len(ar)-1
    # mid = (s+(e-s)//2)
    while(s <= e):
        mid = (s+(e-s)//2)
        if k == ar[mid]:
            return mid
        else:
            if ar[mid] < k:
                s = mid+1
            else:
                e = mid-1
    return False


lis = list(map(int, input("Enter the element of the array: ").split()))
m = int(input("Enter the element which you want to search: "))
print(f"the index of the {m} in the array is ", binearysearch(lis, m))
