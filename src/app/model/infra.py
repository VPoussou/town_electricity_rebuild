class Infra:
    def __init__(self, *args):
        infra_id, infra_type, nb_maisons, longueur = args
        self.infra_id = infra_id
        self.infra_type = infra_type
        self.nb_houses = nb_maisons
        self.length = round(longueur, 2)
        self.difficulty = self.get_infra_difficulty()

    def repair_infra(self):
        # Modifie le type de l'infrastructure,
        # au cas où le type était 'à réparer', alors on le met intact.

        if self.infra_type == 'a_remplacer':
            self.infra_type = 'infra_intacte'
        # return None

    def get_infra_difficulty(self):
        # La difficulté renvoit 0 si si l'infrastructure est intacte.
        # Ou bien calcule la métrique.

        if str(self.infra_type) == 'infra_intacte':
            return 0

        # Ici pour notre métrique, plus la moyenne de notre métrique est élévée,
        # plus çà sera coûteux de raccorder.
        # print(f'Difficulté infrastuctures')
        # print(f' Metrique = longueur_infra/nb_total_maison pour {self.infra_id}')
        metric = self.length / self.nb_houses
        # print(f' => nb_total_maison: {self.nb_houses}')
        # print(f' => longueur_infra: {self.length}')
        # print(f'=> Metric = {metric}')
        # print('-' * 30)

        # return Float
        return metric

    # useful like s = a_infra + b_infra
    def __add__(self, infra):
        # Additionner 2 instances

        if type(infra) != Infra:
            raise Exception("On veut la classe Infra pour pour faire l'ajout avec __add__!")

        # return Float
        return self.difficulty + infra.difficulty

    # Pour radd, on n'appelle pas l'attribut de l'instance
    # Donc pas infra.get_infra_difficulty()
    # useful like s = sum(array_object_of_infra)
    def __radd__(self, infra):
        # Va nous servir dans la classe Batiment
        # print(f'infra: {infra}')
        if type(infra) != Infra:
            raise Exception("On veut la classe Infra pour pour faire l'ajout avec __radd__!")

        # return Float
        # self.set_difficulty()
        return self.difficulty + infra

    def __lt__(self, infra):
        # Pour comparer les batiments en fonction de leur difficulté.

        if type(infra) != Infra:
            raise Exception("On veut la classe Infra pour comparer!")
        # return Bool
        return self.difficulty < infra.difficulty

    def __str__(self):
        return f'Infra Difficulty:{self.difficulty}'
