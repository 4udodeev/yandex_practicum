import sys


class main():
    input_string = sys.stdin.readline().rstrip()

    def is_correct_bracket_seq(input_string):
        stack = []
        braces = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        if len(input_string) == 0:
            return True

        for brace in input_string:
            if brace == '(' or brace == '{' or brace == '[':
                stack.append(brace)
            elif (brace in braces) and (len(stack) != 0) and (braces[brace] == stack[-1]):
                stack.pop()
            else:
                return False
        if len(stack) != 0:
            return False
        else:
            return True

    print(is_correct_bracket_seq(input_string))


if __name__ == '__main__':
    main()
