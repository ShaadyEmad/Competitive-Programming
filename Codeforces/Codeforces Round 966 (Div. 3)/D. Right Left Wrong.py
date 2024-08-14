for _ in range(int(input())):
    length = int(input())
    lst = list(map(int, input().split()))
    directions = input()
    total_sum = sum(lst)
    l,r = 0,length-1
    score = 0
    while l<r:
        if directions[l] == "R":
            total_sum-=lst[l]
            l+=1
        elif directions[r] == "L":
            total_sum-=lst[r]
            r-=1
        else:
            score+=total_sum
            total_sum-=lst[l]
            total_sum-=lst[r]
            l+=1
            r-=1
    print(score)





