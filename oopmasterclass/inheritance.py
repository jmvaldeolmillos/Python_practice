class BasePlayer:
    def __init__(self, hp: int) -> None:
        self.hp = hp

    def walk(self) -> None:
        print("I am walking")


class Wizard(BasePlayer):
    # Sobreescritura
    def walk(self) -> None:
        print("I am floating...")


class Archer(BasePlayer):
    def __init__(self, hp: int, arrows: int) -> None:
        super().__init__(hp)
        self.arrows = arrows

    def shoot(self) -> None:
        self.arrows -= 1
        print(f"Archer shoots... {self.arrows} arrows left!!")


def main() -> None:
    # wizard = Wizard(50)
    # wizard.walk()

    # archer = Archer(100, 5)
    # archer.walk()
    # archer.shoot()

    x = {"test": 123}

    print(x)


if __name__ == "__main__":
    main()
