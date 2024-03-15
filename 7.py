k, ar, an = input('Введите рекорд каждого:').split(sep=' ')
if int(k) >= int(ar) and int(k) >= int(an):
    print(k)
elif int(ar) >= int(k) and int(ar) >= int(an):
    print(ar)
else:
    print(an)