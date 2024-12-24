class User:
    """ modelling a user information class"""
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        user_info = f"User's name is {self.first_name} {self.last_name} and age is {self.age}"
        print(user_info)

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, you are welcome to Kalderon Page!")

user_kwaku = User('Kwaku', 'Duah',25)
user_kwaku_info = f"this user with {user_kwaku.first_name} and last name {user_kwaku.last_name} is only {user_kwaku.age}"
print(user_kwaku_info)

user_kwaku.describe_user()
user_kwaku.greet_user()
    
