def longest_unique_substr(str):
    n = len(str)
    res = 0

    for i in range(n):
        visited = [0] * 256

        for j in range(i, n):
            if (visited[ord(str[j])]):
                break
            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True
        visited[ord(str[i])] = False

    return res


str = input()
print(longest_unique_substr(str))
