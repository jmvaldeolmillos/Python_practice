from pydantic import BaseModel


class Bow(BaseModel):
    name: str
    price: float
    damage: int


bow1 = Bow(name="great bow", price=99.89, damage=20)
print(bow1)
