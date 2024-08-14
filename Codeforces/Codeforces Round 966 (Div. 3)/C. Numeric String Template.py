for _ in range(int(input())):
    lst_length = int(input())
    lst = list(map(int, input().split()))
    for __ in range(int(input())):
        s = input() 
        if (len(s) == lst_length) and (len(set(s))==len(set(lst))==len(set(zip(s,lst)))):
            print("YES")
        else:
            print("NO")