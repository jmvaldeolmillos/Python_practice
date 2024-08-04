# Factory
class Archer:
    def __init__(self, hp: int) -> None:
        self.hp = hp

    def walk(self) -> None:
        print("Archer is walking")

    def attack(self) -> None:
        print("Archer is attacking")


class Knight:
    def __init__(self, hp: int) -> None:
        self.hp = hp

    def walk(self) -> None:
        print("Knight is walking")

    def attack(self) -> None:
        print("Knight is attacking")

# No haria falta usar una clase, se puede usar una simple función
class CharacterFactory:
    def create_character(self, character_type: str, hp: int) -> Archer | Knight:
        if character_type == "archer":
            return Archer(hp)
        elif character_type == "knight":
            return Knight(hp)
        else:
            raise ValueError(f"Invalid character type: {character_type}")

factory = CharacterFactory()
archer = factory.create_character("archer", 100)
knight = factory.create_character("knight", 200)

archer.walk()
archer.attack()
knight.walk()
knight.attack()

# Patrón de Behavioural - Strategy

