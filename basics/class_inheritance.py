# class inheritance using the super() function

class medium_user:
    def __init__(self, name, surname, username, email, subscriber=True):
        self.Name = name
        self.Surname = surname
        self.Username = username
        self.Email = email
        self.Subscriber = subscriber

    def read(self):
        print("{} {} is reading a story".format(self.Name, self.Surname))

    def clap(self):
        print("{} {} clapped a story".format(self.Name, self.Surname))

    def is_member(self):
        if (self.Subscriber==False):
            print("Become a member to get unlimited stories on Medium")
        else:
            print('You are a member')


class medium_subscriber(medium_user):
    pass


jeff = medium_subscriber("Jeff", "Grimm", "jeff-grimm", "jeffgrim@gmail.com")
print(jeff.Name)
jeff.read()
jeff.clap()
jeff.is_member()


# craig = medium_user('Craig', 'Dejean', 'craig-dejean', 'cdejeantsuno@icloud.com', False)
# print(craig.Username)
# craig.read()
# craig.clap()
# craig.is_member()