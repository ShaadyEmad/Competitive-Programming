import re

t = int(input())

for case in range(t):
    txt = []
    for i in range(8):
        input_txt = input()
        pattern = r'[a-z]'
        new = re.findall(pattern, input_txt)
        txt.append(new)

    flattened_list = [item for sublist in txt for item in sublist]
    result_string = ''.join(flattened_list)
    print(result_string)
