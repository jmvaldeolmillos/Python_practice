from enum import Enum


class Weapons(Enum):
    S = "Sword"
    B = "Bow"
    A = "Axe"


bow = Weapons("Bow")
print(bow)
print(bow.value)
