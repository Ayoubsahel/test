class Utilisateur:
    compteur_id = 1
    def __init__(self,nom,age):
        self.__id =  Utilisateur.compteur_id
        self.__nom = nom
        self.__age = age
