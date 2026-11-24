
class User:
    def __init__(self, user_id, username, email, role):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role

    def display_user(self):
        print("User ID:", self.user_id)
        print("Username:", self.username)
        print("Email:", self.email)
        print("Role:", self.role)


user1 = User(1, "dharshan", "dharshan@example.com", "Developer")

user1.display_user()
