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
    def __init__(self, s_name, s_surname, s_username, s_email, begindate, type_membership, payment_method):
        super().__init__(s_name, s_surname, s_username, s_email)
        
        self.Begindate = begindate
        self.Type_membership = type_membership
        self.Payment_method = payment_method

tim = medium_subscriber('Tim', 'Johnson', 'tim-johnson', 'timjohnson@gmail.com', 'March 2019', 'monthly', 'venmo')
print(tim.Username)
print(tim.Begindate)
tim.read()
tim.clap()
tim.is_member()


# this functions below need to call the child classes new attributes in order to work, otherwise you will get an error


# jeff = medium_subscriber("Jeff", "Grimm", "jeff-grimm", "jeffgrim@gmail.com")
# print(jeff.Name)
# jeff.read()
# jeff.clap()
# jeff.is_member()


# craig = medium_user('Craig', 'Dejean', 'craig-dejean', 'cdejeantsuno@icloud.com', False)
# print(craig.Username)
# craig.read()
# craig.clap()
# craig.is_member()