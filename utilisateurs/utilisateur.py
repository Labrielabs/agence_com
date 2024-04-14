class Utilisateur:
    def __init__(self,nom,username,mdp):
        self.__nom= nom
        self.__username = username
        self.__mdp = mdp

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def mdp(self):
        return self.__mdp

    @mdp.setter
    def mdp(self, value):
        self.__mdp = value
