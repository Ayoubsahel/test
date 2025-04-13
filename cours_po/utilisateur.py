class Utilisateur:
    compteur_id = 1
    def __init__(self,nom: str,age: int):
        self.__id =  Utilisateur.compteur_id
        self.__nom = nom
        self.__age = age
    

    def __str__(self):
        return f"id:  {self.__id} nom: {self.__nom} age: {self.__age}"
    
    def __repr__(self):
        return f"{self.__id}"
    