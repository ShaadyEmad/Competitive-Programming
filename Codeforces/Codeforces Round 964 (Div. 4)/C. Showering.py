n = int(input())
for _ in range(n):
    n,s,m = map(int, input().split())
    intervals = []
    for i in range(n):
        intervals.append(list(map(int, input().split())))     
      
    flag = False
    for time in range(n):
        if (time == 0 and intervals[time][0]-0>=s) or (intervals[time][0]-intervals[time-1][1]>=s) or (time == n-1 and m - intervals[time][1]>=s):
            flag = True
            break

    print("YES" if flag else "NO")
