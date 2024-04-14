class Employe:
    def __init__(self,nom,prenom,matricule,fonction,departement):
        self.__nom= nom
        self.__prenom = prenom
        self.__matricule= matricule
        self.__fonction= fonction
        self.__departement= departement

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, value):
        self.__matricule = value

    @property
    def fonction(self):
        return self.__fonction

    @fonction.setter
    def fonction(self, value):
        self.__fonction = value

    @property
    def departement(self):
        return self.__departement

    @departement.setter
    def departement(self, value):
        self.__departement = value