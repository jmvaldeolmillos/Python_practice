user_input = input("Enter value: ")
try:
    number = float(user_input)
except ValueError:
    print("Error de valor")
except:  # noqa: E722
    print("otro...")
