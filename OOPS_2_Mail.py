class gmail_ops:
    def __init__(self,username,password):
        self.username = username
        self.password = password


    def login(self):
        print('Take user id' +  " " + self.username + " " + "take password" + " " + self.password)
        print("Login")

    def read_mail(self):
        print("Read mail for" + self.username + " " + self.password)

    def reply_mail(self):
        print("Reply mail for" + self.username + " " + self.password)


user1 = gmail_ops("user1", "user1pass")

user1.login()