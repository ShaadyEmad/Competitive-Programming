def check_seats():
    length = int(input())
    seats = list(map(int, input().split()))
    if seats == 1:
        return "YES"
    else:
        occupied_seats = set([seats[0]])
        for i in range(1,length-1):
            if (seats[i]-1 in occupied_seats) or (seats[i]+1 in occupied_seats):
                occupied_seats.add(seats[i])
                continue
            else:
                return "NO"
        return "YES"
    
for _ in range(int(input())):
    print(check_seats())
