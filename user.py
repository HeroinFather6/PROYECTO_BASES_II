class User:

    def __init__(self, id, passwrd):
        self.id = id
        self.passwrd = passwrd

        self.connected = False

        User.numUsers += 1
