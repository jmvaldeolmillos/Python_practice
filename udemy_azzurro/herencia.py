class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} is eating.")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping.")


class Cat(Animal):
    def __init__(self, name: str, weigth: float) -> None:
        super().__init__(name)
        self.weigth = weigth

    def meow(self):
        print(f"{self.name} says 'meow'.")


class Dog(Animal):
    def __init__(self, name: str, weigth: float) -> None:
        super().__init__(name)
        self.weigth = weigth

    def guau(self):
        print(f"{self.name} says 'guau'.")


if __name__ == "__main__":
    cat: Cat = Cat("Apple", 100)
    cat.meow()
    cat.sleep()

    dog: Dog = Dog("Doggy", 300)
    dog.sleep()
    dog.eat()
    dog.guau()
