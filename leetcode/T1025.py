def innate(self, n):
    if n < 2:
        return False
    if n == 2:
        return True
    for x in range(1, n):
        if n % x == 0:
            n -= x
            break
    if n == 2:
        return False
    for x in range(1, n):
        if n % x == 0:
            n -= x
            break
    return innate(self, n)


if __name__ == '__main__':
    print(innate("A", 2))
