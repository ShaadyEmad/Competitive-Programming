import math

for _ in range(int(input()) ):
    l = int(input())
    s = input()
    root = math.isqrt(l)
    if root*root == l:
        print("NO")
    else:
        zeros = s.count("0")
        broder_elements = 4*(root-1)
        if (zeros > l - broder_elements) or (zeros==0 and broder_elements!=l):
            print("NO")
        else:
            print("YES")
