nums = int(input())
tries = 5

for i in range (nums):
    result = 1
    a,b,c = map(lambda x: int(x), input().split())
    for _ in range(tries):
        if a<=b and a<=c:
            a+=1
        elif b<=a and b<=c:
            b+=1
        else:
            c+=1
        
    result = a*b*c
    print(result)
