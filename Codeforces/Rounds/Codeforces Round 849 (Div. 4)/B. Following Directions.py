n = int(input())


def movement(moves):
    x_y = [0, 0]
    for i in range(length):
        if moves[i] == "U":
            x_y[0] += 1
        elif moves[i] == "D":
            x_y[0] -= 1
        elif moves[i] == "R":
            x_y[1] += 1
        else:
            x_y[1] -= 1

        if x_y == [1,1]:
            print("YES")
            break

    if x_y != [1, 1]:
        print("NO")

for _ in range(n):
    length = int(input())
    moves = input()
    movement(moves)
