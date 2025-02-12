def main(input_str: str) ->str:
    try:
        a, op, b = input_str.split()
        a, b = int(a), int(b)
        if a not in range(1, 11) or b not in range(1, 11):
            raise ValueError("Ошибка: число вне диапазона")

        elif op == '+': return str(a + b)
        elif op == '-': return str(a - b)
        elif op == '*': return str(a * b)
        elif op == '/': return str(a // b)
        else:
            raise ValueError('Ошибка: неверная операция')

    except ValueError:
        return('Ошибка: неверная операция')

result = main("8 * 1")
print(result)