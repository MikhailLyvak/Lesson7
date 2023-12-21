# Ініціалізуйте клас з ім'ям "Person", який при ініціалізації отримує параметр "name" і "age" і напишіть метод is_adult, який повертає True якщо людина повнолітня і False якщо ні.


# ==============================================================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        return self.age >= 18     
    
           
        
        
# ==============================================================================


# Для перевірки
person = Person(name="Михайло", age=18)
print(person.is_adult())

person = Person(name="Михайло", age=17)
print(person.is_adult())
