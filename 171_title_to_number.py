def title_to_number(title: str) -> int:
    total = 0
    idx = 0

    for i in title[::-1]:
        total += (ord(i) - 64) * 26 ** idx
        idx += 1
    return total

print(title_to_number("AB"))
