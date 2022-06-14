# pos = (x, y)
# mouvement = ( (x1, y1), (x2, y2) )


default_ligne_vide      = "........"
default_ligne_piecesN   = "tcfdrfct"
default_ligne_piecesB   = "tcfrdfct"
default_ligne_pions     = "pppppppp"

default_plateau = [ 
    [ [x] for x in default_ligne_piecesN ],
    [ [x] for x in default_ligne_pions ],
    [ [x] for x in default_ligne_vide ],  
    [ [x] for x in default_ligne_vide ],
    [ [x] for x in default_ligne_vide ],  
    [ [x] for x in default_ligne_vide ],
    [ [x] for x in default_ligne_pions.upper() ],
    [ [x] for x in default_ligne_piecesB.upper() ],
]

plateau = default_plateau

def print_tableau(liste):
    for ligne in liste:
        for piece in ligne:
            print(piece[0] + " ", end="")
        print()    

def valeurs_camps(liste):
    valeur_blanc = 0
    valeur_noir = 0
    valeurs = {
        "p":1,
        "P":1,
        "T":5,
        "t":5,
        "C":3,
        "c":3,
        "F":3,
        "f":3,
        "D":9,
        "d":9,
        "R":0,
        "r":0,
    }
    for ligne in liste:
        for piece in ligne:
            piece = piece[0]
            if piece.isupper():
                valeur_blanc += valeurs[piece]
            elif piece.islower():
                valeur_noir += valeurs[piece]
    return({"p_blanc":valeur_blanc, "p_noir":valeur_noir, "diff":valeur_blanc-valeur_noir})

def pos_valide(liste, pos):
    if 0 <= pos[0] <= len(liste) and 0 <= pos[1] <= len(liste[0]):
        return True
    return False

def piece_pos(liste, pos):
    if pos_valide(liste, pos):
        return liste[pos[0]][pos[1]][0]

def mouvement_valide():
    return True

def mouvement_piece(liste, mouvement):
    listex = [liste]
    if mouvement_valide():
        liste[mouvement[1][0]][mouvement[1][1]] = piece_pos(liste, mouvement[0])
        liste[mouvement[0][0]][mouvement[0][1]] = "."
    return liste

actions_mouvements = [
    ((0, 0), (5,1)),
    ((5,1), (3,1)),
]

for id_mouvement in range(len(actions_mouvements)):
    plateau = mouvement_piece(plateau, actions_mouvements[id_mouvement])
    print_tableau(plateau)
    print(str(id_mouvement))

print()
#print_tableau(plateau)