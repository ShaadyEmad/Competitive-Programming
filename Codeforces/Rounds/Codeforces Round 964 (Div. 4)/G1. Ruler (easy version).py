for _ in range(int(input())):
    low,high  = 2, 999
    while low < high:
        mid = (low+high)//2
        print("?",1,mid)
        ans = int(input())
        if ans == mid:
            low = mid+1
        else:
            high = mid

    print("!",low)
