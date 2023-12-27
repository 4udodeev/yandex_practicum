# ID успешной посылки - 103960421

class main():
    weights_list: list = list(map(int, input().split()))
    limit: int = int(input())

    def calculate_platforms(weights: list[int], limit: int) -> int:
        """Функция расчета оптимального количества платформ"""
        platforms: int = 0

        correct_weights: list = [elem for elem in weights if elem <= limit]
        correct_weights.sort()
        if len(correct_weights) == 0:
            return 0
        if len(correct_weights) == 1 and correct_weights[0] <= limit:
            return 1

        left_index: int = 0
        right_index: int = len(correct_weights)-1

        while left_index < right_index:
            if correct_weights[right_index] == limit:
                platforms += 1
                right_index -= 1
            elif (correct_weights[left_index] + correct_weights[right_index]
                  <= limit):
                platforms += 1
                right_index -= 1
                left_index += 1
            else:
                platforms += 1
                right_index -= 1
            if (left_index == right_index
               and correct_weights[left_index] <= limit):
                platforms += 1

        return platforms

    print(calculate_platforms(weights_list, limit))


if __name__ == '__main__':
    main()
