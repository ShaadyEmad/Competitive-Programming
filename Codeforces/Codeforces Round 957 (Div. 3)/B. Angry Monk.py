nums = int(input())

for i in range (nums):
    counter = 0
    n, k = map(lambda x: int(x), input().split())
    lst = list(map(lambda x: int(x), input().split()))
    max_piece = max(lst)
    lst.remove(max_piece)    
    for i in range(k-1):
        if lst[i] == 1:
            counter +=1
        elif lst[i] == 2:
            counter +=3
        else:
            counter += (lst[i]-1) + (lst[i])
            
    print(counter)
