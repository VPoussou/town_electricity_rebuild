class Batiment:
    def __init__(self, *args):
        id_batiment, list_infras = args

        self.id_building = id_batiment
        # liste de class Infra
        self.list_infras = list_infras

        self.difficulty = self.get_building_difficulty()

    def get_building_difficulty(self):
        # La metrique: somme des difficultés des infras

        # Méthode 1: (Recommended)
        # On additione directement
        # les object si on a la méthode __radd__ dans la classe Infra
        # metrique = sum(self.list_infras)

        # Methode 2:
        # on additionne en appelant les attributs
        metrique = 0
        for infra in self.list_infras:
            metrique += infra.difficulty

        # return metrique
        # return float value
        return metrique

    def __lt__(self, batiment):
        # Pour comparer les batiments en fonction de leur difficulté.

        if type(batiment) != Batiment:
            raise Exception("On veut la classe Batiment pour comparer!")
        # return Bool
        return self.difficulty < batiment.difficulty

    def __str__(self):
        return f'Batiment Difficulty:{self.difficulty}'
