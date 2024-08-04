# Slots se usa declarar una cantidad fija de atributos para una clase
# optimización de memoria si habrá un gran número de objetos de dicha clase
# da problemas con la herencia tendremos que añadir otro __slots__ con las nuevas vars

from pympler import asizeof


class Archer:
    __slots__ = ("hp", "mana")

    def __init__(self, hp: int, mana: int) -> None:
        self.hp = hp
        self.mana = mana


class Archer2:
    def __init__(self, hp: int, mana: int) -> None:
        self.hp = hp
        self.mana = mana


archer1 = Archer(100, 50)
# print(archer1.__dict__) Da error con slots
# archer1.arrows = 10 -> da error si no está en slots

archer2 = Archer2(200, 100)

# vamos a ver la diferencia entre usar slots y no usarlo...
print(asizeof.asizeof(archer1))  # da 112
print(asizeof.asizeof(archer2))  # da 504
