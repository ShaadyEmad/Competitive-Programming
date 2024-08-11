n = int(input())
for _ in range(n):
    a1,a2,b1,b2 = map(int, input().split())
    suneet_wins = 0

    if (a1 > b1 and a2 >= b2) or (a1 >= b1 and a2 > b2):
        suneet_wins+=2

    if (a1 > b2 and a2 >= b1) or (a1 >= b2 and a2 > b1):
        suneet_wins+=2

    print(suneet_wins) 
