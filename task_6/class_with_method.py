# Ініціалізуйте клас з ім'ям "Person", який при ініціалізації отримує параметр "name" і "age" і напишіть метод is_adult, який повертає True якщо людина повнолітня і False якщо ні.


# ==============================================================================
#     Пиши свій код тут ( відчувай себе вільно щоб стерти цей комментар)
# ==============================================================================


# Для перевірки
person = Person(name="Михайло", age=18)
print(person.is_adult())

person = Person(name="Михайло", age=17)
print(person.is_adult())
