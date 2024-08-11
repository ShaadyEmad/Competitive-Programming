t = int(input())
for _ in range(t):
    xc, yc, k = map(int, input().split())
    
    points = [(xc+i, yc-i) for i in range(k)]
    sum_x_coords = sum(x for x, y in points)
    sum_y_coords = sum(y for x, y in points)
    
    target_sum_x = k * xc
    target_sum_y = k * yc
    
    for i in range(k):
        if sum_x_coords != target_sum_x:
            diff_x = target_sum_x-sum_x_coords
            points[i] = (points[i][0]+diff_x, points[i][1])
            sum_x_coords += diff_x
        
        if sum_y_coords != target_sum_y:
            diff_y = target_sum_y-sum_y_coords
            points[i] = (points[i][0], points[i][1]+diff_y)
            sum_y_coords += diff_y
            
        if sum_x_coords == target_sum_x and sum_y_coords == target_sum_y:
            break
            
    for point in points:
        print(f"{point[0]} {point[1]}")
