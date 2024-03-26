# we use Pascal name convention for class names and snake_case for almost everything else
# Attributes are the things that the object has
# Methods are the things that the object does
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "John")
user_2 = User("002", "Mina")
user_3 = User("003", "Sara")
user_4 = User("004", "Nick")

user_1.follow(user_2)
user_1.follow(user_3)

user_4.follow(user_2)

print(f"{user_1.username} has {user_1.followers} followers")
print(f"{user_1.username} has {user_1.following} following")


print(f"{user_2.username} has {user_1.followers} followers")
print(f"{user_2.username} has {user_1.following} following")

