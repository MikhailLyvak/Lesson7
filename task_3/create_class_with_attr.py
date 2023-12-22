# Ініціалізувати класс User з можливістю внести туди такі значення username, first_name, last_name

        
# ==============================================================================
class User(): 
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

# ==============================================================================


# Для перевірки
user = User(username="Mishakarisha", first_name="Misha", last_name="Lyvak")

print(user.username)
print(user.first_name)
print(user.last_name)
