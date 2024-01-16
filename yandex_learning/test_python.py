def max_blocks_to_sort(n, arr):
    max_blocks = 1
    max_val = max(arr[0:arr.index(0)])

    for i in range(arr.index(0), n):
        max_val = max(max_val, arr[i])

        if max_val == i:
            max_blocks += 1

    return max_blocks


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(max_blocks_to_sort(n, arr))
