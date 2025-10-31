from errors import AgeTooBigError, AgeIsNegativeError

def getName() -> str:
    while True:
        try:
            name = input("Введите имя: ")

            if not name.isalpha():
                raise Exception("имя должно состоять только из букв")

            return name
        except Exception as e:
            print("Ошибка:", e)


def getAge() -> int:
    while True:
        try:
            age = int(input("Введите ваш возраст: "))

            if age > 100:
                raise AgeTooBigError("возраст не может быть больше 100")
            if age < 0:
                raise AgeIsNegativeError("возраст не может быть отрицательным")

            return age
        
        except AgeTooBigError as ATBE:
            print("Ошибка:", ATBE)
        except AgeIsNegativeError as EINE:
            print("Ошибка:", EINE)
        except ValueError:
            print("Ошибка: возраст должен быть числом")

def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    return False
