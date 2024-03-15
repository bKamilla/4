first, second = input('Введите счет двух команд:').split(sep=':')
if first < second:
    print(2)
elif second < first:
    print(1)
else:
    print(0)