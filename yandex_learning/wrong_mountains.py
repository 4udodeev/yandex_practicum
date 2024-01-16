import sys


class main():
    peaks_array: list = list(map(int, sys.stdin.readline().rstrip().split()))

    def valid_mountain_array(peaks_array: list) -> bool:
        """Функция проверки правильности горы."""
        if len(peaks_array) < 3:
            return False
        elif peaks_array[0] > peaks_array[1]:
            return False

        up: bool = True
        down: bool = False
        count: int = 0

        while up:
            for index in range(len(peaks_array)-1):
                if peaks_array[index] < peaks_array[index+1]:
                    count += 1
                elif peaks_array[index] == peaks_array[index+1]:
                    return False
                else:
                    up = False
                    down = True
            up = False
            if not down:
                return False

        while down:
            for index in range(count, len(peaks_array)-1):
                if peaks_array[index] == peaks_array[index+1]:
                    return False
                elif peaks_array[index] < peaks_array[index+1]:
                    return False
            down = False

        return True

    print(valid_mountain_array(peaks_array))


if __name__ == '__main__':
    main()
