for _ in range(int(input())):
    n = int(input())
    answer = input()
    score = 0
    for choice in "ABCD":
        score += min(n,answer.count(choice))

    print(score)
