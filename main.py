def math(a, b, c):
    d = (b*b - 4*a*c)
    if d < 0: print('Корней нет')
    else:
        x1 = (-b + d ** 0.5) / (2*a)
        x2 = (-b - d ** 0.5) / (2*a)
        print(x1, x2)


a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))
math(a, b, c)
