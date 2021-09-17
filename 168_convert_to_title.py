def convert_to_title(n: int) -> str:
    output = []
    while n > 0:
        if n % 26 == 0:
            output.append('Z')
            n = (n // 26) - 1
        else:
            output.append(chr((n % 26) + 64))
            n = n // 26

    return "".join(output[::-1])


for i in range(100):
    print(convert_to_title(i))
