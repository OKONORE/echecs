class Piece:
    def __init__(self, Type: str, Couleur: str, Orientation: tuple(int, int)):
        self.Type = Type
        self.Couleur = Couleur
        self.Orientation = Orientation
    def valeur(self):
        valeurs = {
            "Pion":1,
            "Tour":5,
            "Cavalier":3,
            "Fou":3,
            "Roi":0,
            "Dame":9,
        }
        if self.Type in valeurs:
            return valeurs[self.Type]
        return None

    def deplacer(self, position, echequier):
        if self.Type = Pion:

class Echequier:
    def __init__(self, taille_cote):
        self.taille_cote = taille_cote
        self.echequier = [[None for _ in range(self.taille_cote)] for _ in range(self.taille_cote)]
    
    def print(self):
        for ligne in self.echequier:
            for case in ligne:
                if case == None:
                    print("  ", end="|")
                else:
                    print(case.Type[:2], end='|')
            print()
            print("-"*self.taille_cote*3)

    def points(self):
        dico_points = dict()
        for ligne in self.echequier:
            for case in ligne:
                if case != None:
                    if case.Couleur in dico_points:
                        dico_points[case.Couleur] += case.valeur()
                    else:
                        dico_points[case.Couleur] = case.valeur()
        return dico_points

def main():
    ECHEQUIER = Echequier(8)
    ECHEQUIER.echequier = [
        [Piece(nom, "Noir") for nom in ["Tour", "Cavalier", "Fou", "Dame", "Roi", "Fou", "Cavalier", "Tour"]],
        [Piece("Pion", "Noir") for _ in range(8)],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Piece("Pion", "Blanc") for _ in range(8)],
        [Piece(nom, "Blanc") for nom in ["Tour", "Cavalier", "Fou", "Dame", "Roi", "Fou", "Cavalier", "Tour"]],
    ]

    ECHEQUIER.print()

main()