from abc import ABC, abstractclassmethod


class Phone(ABC):
    def __init__(self, model: str) -> None:
        self.model = model


@abstractclassmethod
def power(self): ...


@abstractclassmethod
def call_target(self, person: str): ...


class iBanana(Phone):
    def __init__(self, model: str) -> None:
        super().__init__(model)

    @property
    def power(self):
        pass

    def call_target(self, person: str):
        pass


phone = Phone("iBanana")
