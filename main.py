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
    name: str = getName()
    age: int = getAge()

    print(f"Привет, {name}! Тебе {age} лет.")
    if is_adult(age):
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")

main()