def check(x, a):
    new_total_sum = total_sum + x
    avg = new_total_sum / n
    unhappy_count = sum(1 for w in a if w < avg / 2)
    if max_wealth + x < avg / 2:
        unhappy_count += 1
    return unhappy_count > n / 2


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total_sum = sum(a)
    max_wealth = max(a)
    if n in[1,2]:
        print(-1)
    else:
        left, right = 0, 10**12
        if check(0, a):
            print(0)
            continue

        while left < right:
            mid = (left + right) // 2
            if check(mid,a):
                right = mid
            else:
                left = mid + 1
        
        if left < 10**12:
            print(left)
        else:
            print(-1)
