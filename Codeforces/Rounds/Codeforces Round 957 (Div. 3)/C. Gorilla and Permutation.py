nums = int(input())

for i in range (nums):
    n, m, k = map(lambda x: int(x), input().split())
    numbers = list(range(n, 0, -1))
    m_index = numbers.index(m)
    new_lst = sorted(numbers[m_index:]) 
    numbers[m_index:] = new_lst   
    print(*numbers)
