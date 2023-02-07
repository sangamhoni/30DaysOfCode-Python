class User:
    # pass
    # write the classname in PascalCase

    def __init__(self, user_id, username):
        # attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
# we can just set smth to default value and we dont have to pass it to initialiser

    # methods
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'angela')
user_2 = User('002', 'jack')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
