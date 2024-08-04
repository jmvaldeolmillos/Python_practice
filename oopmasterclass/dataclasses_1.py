# Clases que únicamente tienen atributos
from dataclasses import dataclass


class Bow:
    def __init__(self, name: str, price: int, damage: int) -> None:
        self.name = name
        self.price = price
        self.damage = damage


bow_a = Bow("great bow", 100, 20)
print(bow_a.__dict__)


@dataclass(frozen=True, order=True, repr=False)
class Bow2:
    name: str
    price: float
    damage: int


bow1 = Bow2("great bow2", 99, 20)
print(bow1)
