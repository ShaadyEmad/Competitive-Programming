t = int(input())

for case in range(t):
    a, b, c = map(int, input().split())
    if (a + b >= 10) or (a + c >= 10) or (b + c >= 10):
        print("YES")
    else:
        print("NO")
