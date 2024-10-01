class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_credentials(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)


class Student(User):
    def __init__(self, username, password, first_name, last_name):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name



def login(users, entered_username, entered_password):
    for user in users:
        if user.verify_credentials(entered_username, entered_password):
            return user
    return None
