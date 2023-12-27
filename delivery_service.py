# ID успешной посылки - 103960421

def calculate_platforms(weights: list[int], limit: int) -> int:
    """Функция расчета оптимального количества платформ"""
    platforms: int = 0
    sorted_weights: list = sorted(weights)
    left_index: int = 0
    right_index: int = len(sorted_weights)-1

    while left_index <= right_index:

        if (sorted_weights[left_index] + sorted_weights[right_index]
                <= limit):
            left_index += 1

        platforms += 1
        right_index -= 1

    return platforms


if __name__ == '__main__':
    weights_list: list = [int(elem) for elem in input().split()]
    limit: int = int(input())

    print(calculate_platforms(weights_list, limit))
