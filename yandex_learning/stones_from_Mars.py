def count_matching_customers(orders, delivered):
    # Сортируем списки, чтобы упростить сравнение
    orders.sort()
    delivered.sort()

    i = j = 0  # Индексы для обхода списков
    count = 0  # Счетчик совпадающих элементов

    # Идем по обоим спискам и сравниваем элементы
    while i < len(orders) and j < len(delivered):
        if delivered[j] >= orders[i]:
            count += 1
            i += 1
        j += 1

    return count

# Считываем данные
n = int(input())
orders = list(map(int, input().split()))
m = int(input())
delivered = list(map(int, input().split()))

# Выводим результат
result = count_matching_customers(orders, delivered)
print(result)
