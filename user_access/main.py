from validators import getName, getAge, is_adult

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

if __name__ == "__main__":
    main()