from collections import Counter


def custom_sort(arr, pattern):
    pattern_counts = Counter(pattern)
    result = []
    # Поместить элементы в соответствии с шаблоном
    for p in pattern:
        if p in arr:
            result.extend([p] * arr.count(p))
    # Добавить элементы, не упомянутые в шаблоне, и отсортировать их
    extras = sorted([x for x in arr if x not in pattern])
    result.extend(extras)
    return result

# Пример использования функции
count_arr = int(input())
arr = [int(i) for i in input().split(' ')]
count_pattern = int(input())
if count_pattern > 0:
    pattern = [int(i) for i in input().split(' ')]
    result = custom_sort(arr, pattern)
else:
    result = []
    extras = sorted([x for x in arr])
    result.extend(extras)
print(' '.join(str(i) for i in result))
