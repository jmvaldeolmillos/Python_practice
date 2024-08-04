# getters y setters para un montón de atributos?


class Deskriptor:
    def __get__(self, instance, owner) -> int:
        return instance.__dict__[self.name]

    def __set__(self, instance, value: int) -> None:
        if value < 0 or value > 100:
            raise ValueError("Value has to ve between 0 and 100.")
        instance.__dict__["value"] = value


# Usaremos el deskriptor protocol
class Archer:
    # podemos dejarlo como arriba, o utilizar un constructor.
    def __init__(self, hp: int, mana: int) -> None:
        self.hp = hp
        self.mana = mana


archer1 = Archer(100, 30)
print(archer1.__dict__)
