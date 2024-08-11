t = int(input())

for case in range(t):
    num = int(input())
    lst = []
    for i in range(num):
        a, b = map(int, input().split())
        if a <= 10:
            lst.append([b])
        else:
            lst.append([])
            pass
    max_num = max(lst)
    max_num_index = lst.index(max_num)
    print(max_num_index + 1)
