# ID посылки 104964722
def decode_instructions(input_instruction: str) -> str:
    previous_instruction_stack: list[tuple[str, int]] = []
    current_number: int = 0
    current_instruction: str = ''

    for symbol in input_instruction:
        if symbol.isdigit():
            current_number = current_number * 10 + int(symbol)
        elif symbol.isalpha():
            current_instruction += symbol
        elif symbol == '[':
            previous_instruction_stack.append((current_instruction,
                                               current_number))
            current_instruction = ''
            current_number = 0
        elif symbol == ']':
            prev_instruction, repeat_count = previous_instruction_stack.pop()
            current_instruction = (prev_instruction
                                   + current_instruction * repeat_count)

    return current_instruction


if __name__ == '__main__':
    input_instruction: str = input()
    print(decode_instructions(input_instruction))
