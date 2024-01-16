def find_winner(n, k):
    if n == 1:
        return 1
    else:
        return (find_winner(n - 1, k) + k-1) % n + 1


def main():
    n = int(input())
    k = int(input())
    winner = find_winner(n, k)
    print(winner)


if __name__ == "__main__":
    main()