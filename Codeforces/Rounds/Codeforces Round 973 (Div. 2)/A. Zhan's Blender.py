import math
for _ in range(int(input())):
    n = int(input()) 
    x, y = map(int, input().split())
    print(math.ceil(n / min(x, y)))
