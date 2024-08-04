# antes del / no se pueden pasar como keys, solo posicionales, despues como queramos.


def myfunction(p1, p2, /, p3):
    print(p1, p2, p3)


myfunction(12, 12, 12)
myfunction(12, 12, p3=12)

# despues del * solo se puede poner con keys, no posicionales.


def myfunction(p1, p2, *, p3):
    print(p1, p2, p3)


myfunction(12, 12, 12)
myfunction(12, 12, p3=12)
