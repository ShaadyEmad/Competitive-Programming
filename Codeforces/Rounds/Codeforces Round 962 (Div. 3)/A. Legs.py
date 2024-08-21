n = int(input())
for _ in range(n):
    animals = 0
    legs = int(input())
    while legs != 0:
        if legs % 4 == 0:
            legs -= 4
            animals +=1
        else:
            legs -= 2
            animals +=1
            
    print(animals)
