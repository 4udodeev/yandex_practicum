class main():

    array = list(map(int, input().split()))

    def find_low_count(array: list) -> list:
        result_array = []
        for a in range(len(array)):
            count = 0
            for b in range(len(array)-1):
                if array[a] > array[b]:
                    count += 1
            result_array.append(count)
        return result_array

    print(find_low_count(array))


if __name__ == '__main__':
    main()
