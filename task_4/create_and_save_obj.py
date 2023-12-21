# Ініціалізуйте класс Profile з такими аргументами user_id, phone і створіть обєкт в user_profile1 в який внесить данні на свій вибір відповідно до аргументів які приймає цей класс


# ==============================================================================
class Profile:
    def __init__(self, user_id, phone):
        self.user_id = user_id
        self.phone = phone
    def __int__(self):
        return f"{self.user_id} {self.phone}"
        
user_profile1 = Profile("1", phone="12345678")
        
# ==============================================================================


# Для перевірки
print(user_profile1.user_id)
print(user_profile1.phone)
