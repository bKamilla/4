first, second = input('Введите счет двух команд:').split(sep=':')
if int(first) < int(second):
    print(2)
elif int(second) < int(first):
    print(1)
else:
    print(0)