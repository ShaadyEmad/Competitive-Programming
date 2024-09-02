import math

def check_square(n):
    root = int(math.sqrt(n))
    return root * root == n, root

t = int(input())
for _ in range(t):
    l = int(input())
    s = input()
    check, root = check_square(l)
    if not check:
        print("NO")
    else:
        borders = 4 * (root - 1)
        zeros = l - borders
        zeros_count = s.count("0")
        if borders == l or zeros_count == zeros:
            print("YES")
        else:
            print("NO")
