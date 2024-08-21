n = int(input())

def opertation(binary_input):
    for i in range(length):
        try:
            if (binary_input[0] == '1' and binary_input[-1] == '0') or (binary_input[0] == '0' and binary_input[-1] == '1'):
                del binary_input[0]
                del binary_input[-1]
            else:
                break
        except IndexError:
            break

    print(len(binary_input))

for _ in range(n):
    length = int(input())
    binary_input = list(input())
    opertation(binary_input)
