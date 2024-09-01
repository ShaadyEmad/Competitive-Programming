import math
for _ in range(int(input())):
    l, r = map(int, input().split())
    max_sum = r - l
    k = math.floor((math.sqrt(1 + 8 * max_sum) - 1) / 2)
    print(k + 1)
