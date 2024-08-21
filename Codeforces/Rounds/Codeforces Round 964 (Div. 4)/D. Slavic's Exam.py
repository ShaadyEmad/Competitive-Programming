t = int(input())

for _ in range(t):
    word1 = list(input())
    word2 = list(input())
    word2_len = len(word2)
    j = 0
    for i in range(len(word1)):
        if j >= word2_len:
            break
        if word1[i] == word2[j%word2_len]:
            j+=1
        elif word1[i] == "?":
            word1[i] = word2[j%word2_len]
            j+=1

    word1 = "".join(word1).replace("?", "a")
    if j ==  word2_len:
        print("YES")
        print(word1)
    else:
        print("NO")
