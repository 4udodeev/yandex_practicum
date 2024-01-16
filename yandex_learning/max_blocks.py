def max_blocks_count(n, array):
    max_blocks = 0
    current_max = 0

    for i in range(n):
        current_max = max(current_max, array[i])

        if current_max == i:
            max_blocks += 1

    return max_blocks

# Считываем данные
n = int(input())
array = list(map(int, input().split()))

# Выводим результат
print(max_blocks_count(n, array))
