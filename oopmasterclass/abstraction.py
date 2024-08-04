from abc import ABC, abstractmethod


class AbstractArcher(ABC):
    @abstractmethod
    def walk(self):
        print("I walk...")

    @property
    @abstractmethod
    def hp(self):
        pass


class Archer(AbstractArcher):
    def __init__(self, hp: int) -> None:
        super().__init__()
        self._hp = hp

    def walk(self):
        super().walk()

    @property
    def hp(self) -> int:
        return self._hp


archer = Archer(12)
archer.walk()
print(archer.hp)
