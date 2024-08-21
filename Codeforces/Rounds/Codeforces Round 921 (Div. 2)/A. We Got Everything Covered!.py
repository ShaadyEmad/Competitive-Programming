for _ in range(int(input())):
    n, k = map(int, input().split())
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = alpha[:k]
    
    for i in range(n):
        print(result,end='')
    
    print("")
