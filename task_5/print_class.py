# Ініалізуйте класс Person з атрибутами first_name, last_name і додайте строкову репрезентація __str__ щоб при прінті обєкту в консоль виводилось
# Всім привіт, мене звати Михайло Ливак


# ==============================================================================
class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name 
        self.last_name = last_name
    def __str__(self):
        return f"Всім привіт, мене звати {self.first_name} {self.last_name} "
# ==============================================================================


# Для перевірки
person = Person(first_name="Михайло", last_name="Ливак")
print(person)
