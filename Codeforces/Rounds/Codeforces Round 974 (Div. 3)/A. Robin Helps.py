for _ in range(int(input())):
    n,k = map(int, input().split())
    lst = list(map(int, input().split()))
    gold = 0
    persons = 0
    for i in lst:
        if i>=k:
            gold+=i
        elif i ==0 and gold >0 :
            persons+=1
            gold-=1
        
    print(persons)
