from typing import Callable

int_function = Callable[[int], int]


def add_three(x: int) -> int:
    return x + 3


def main():
    my_var: int_function = add_three
    print(my_var(5))


if __name__ == "__main__":
    main()
