from typing import Protocol


class Writable(Protocol):
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


class Readable(Protocol):
    def read(self) -> dict:
        """This method should return a dictionary."""


# lo utiliza como un tipo
def do_write(writer: Writable, data: dict) -> None:
    writer.write(data)


# lo utiliza como un tipo
def do_read(reader: Readable) -> dict:
    return reader.read()


class Author:
    def __init__(self, name: str) -> None:
        self.name = name

    def write(self, data: dict) -> None:
        print(f"{self.name} is writing data: {data}")


class ReadWritable(Readable, Writable):
    def __str__(self):
        return f"{self.__class__.__name__}()"


def main():
    data: dict[str, str | int] = {"name": "John Doe", "age": 30}
    author: Author = Author("John Doe")
    uno = "Uno"
    print(uno)
    do_write(author, data)


if __name__ == "__main__":
    main()
