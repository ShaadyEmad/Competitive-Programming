for _ in range(int(input())):
    num = input()
    if len(num) >= 3 and num.startswith('10') and int(num[2:])>=2 and not num[2:].startswith('0'):
        print("YES")
    else:
        print("NO")
