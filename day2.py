def getName():
    print("Введите имя: ", end="")
    return input()

def getAge():
    print("Введите возраст: ", end="")
    return int(input())

def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    return False

def main():

    while True:
        name: str = getName()

        if name.lower() == "стоп":
            print("Выход из программы...")
            break

        age: int = getAge()

        print(f"Привет, {name}! Тебе {age} лет.")
        if is_adult(age):
            print("Доступ разрешен\n")
        else:
            print("Доступ запрещен\n")

main()