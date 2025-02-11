from enum import Enum

# Определение Enum для типа D (byte)
class ByteEnum(Enum):
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3

# Определение класса
class MyClass:
    # Переменная A типа bool
    variable_a: bool = True

    # Константа B типа char
    CONSTANT_B: str = 'A'  # в Python char - это просто строка длины 1

    # Массив C типа ulong
    array_c: list[int] = [1, 2, 3, 4, 5]  # Массив чисел типа ulong

    # Enum D типа byte
    enum_d: ByteEnum = ByteEnum.VALUE1

    def __init__(self):
        # Инициализация значений
        self.variable_a = True
        self.CONSTANT_B = 'Z'
        self.array_c = [1, 2, 3]
        self.enum_d = ByteEnum.VALUE2

    def perform_operations(self):
        # Операции между переменными и константами
        # A - B: Сравнение, так как B - это символ (char), а A - bool
        result_ab = self.variable_a and (self.CONSTANT_B == 'A')

        # A - C: Перебор значений в массиве
        result_ac = [self.variable_a and (item > 2) for item in self.array_c]

        # A - D: Преобразование Enum в целое число и сравнение
        result_ad = self.variable_a and (self.enum_d.value > 1)

        print(f"Result of A and B operation: {result_ab}")
        print(f"Result of A and C operation: {result_ac}")
        print(f"Result of A and D operation: {result_ad}")

# Создание объекта класса
my_obj = MyClass()

# Выполнение операций
my_obj.perform_operations()