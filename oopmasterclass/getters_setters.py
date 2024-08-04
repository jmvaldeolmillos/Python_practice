class Archer:
    def __init__(self, hp: int) -> None:
        self.__hp = hp

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, value: int) -> None:
        self.__hp = value

    # el getter y setter manual, bueno para hacer p.e. validaciones
    # def get_hp(self) -> int:
    #     print("getter called")
    #     return self.__hp

    # def set_hp(self, value: int) -> None:
    #     if value > 200:
    #         raise ValueError("HP can be 200 at max!")
    #     print("setter called")
    #     self.__hp = value

    # hp = property(fget=get_hp, fset=set_hp)


archer1 = Archer(100)
archer1.hp = 250
print(archer1.hp)
print(archer1.__dict__)
