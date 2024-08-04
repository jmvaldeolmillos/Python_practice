# Son como grupos de variables.

from enum import Enum


class State(Enum):
    OFF = 0
    ON = 1


state = State.ON

if state == State.ON:
    print("Está encendida")
    print(State.ON.value)
    print(state.name)
    print(state.value)
else:
    print("Está apagada")
