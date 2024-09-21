for _ in range(int(input())):
    n, k = map(int, input().split())
    start_year = max(1, n - k + 1)
    odd_count = (n + 1) // 2 - start_year // 2
    print("YES" if odd_count % 2 == 0 else "NO")
