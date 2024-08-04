import json


class Archer:
    def __init__(self, hp: int) -> None:
        self.hp = hp

    def walk(self):
        return "I am walking."


# mix una
class JsonMixin:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


# otra mix para Archer
class SuperWalkMixin:
    def walk(self):
        return f"{super().walk()} extremely fast!!!"


class SuperArcher(JsonMixin, SuperWalkMixin, Archer):
    pass


a = SuperArcher(100)
print(a.walk())
print(a.toJSON())
