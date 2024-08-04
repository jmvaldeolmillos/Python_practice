user_input = input("Ingrese un número: ")

try:
    number = float(user_input)
except Exception as e:
    print(e)
else:
    print(number)
