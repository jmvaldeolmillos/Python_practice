people: list[str, int] = ["Mario", "Luigi", 10, "Toad", 20, 30]


def is_str(element):
    return isinstance(element, str)


filtered_people: list[str] = list(filter(is_str, people))

print(filtered_people)


def is_int(element):
    return isinstance(element, int)


filtered_people: list[int] = list(filter(is_int, people))

print(filtered_people)
