for _ in range(int(input()) ):
    a, b = map(int, input().split())
    total_sum = a * 1 + b * 2
    
    if total_sum % 2 != 0:
        print("NO")
    else:
        half_sum = total_sum // 2
        if half_sum % 2 == 0 or (half_sum % 2 == 1 and a > 0):
            print("YES")
        else:
            print("NO")
