# pos = (x, y)
# mouvement = ( (x1, y1), (x2, y2) )

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
    if 0 <= pos[0] <= len(liste)-1 and 0 <= pos[1] <= len(liste[0])-1:
        return True
    return False

def piece_pos(liste, pos):
    if pos_valide(liste, pos):
        return liste[pos[0]][pos[1]][0]

def pos_cavalier(liste, pos):
    pos_cavalier = []
    pos_cavalier2 = []
    delta_cavalier = (1, 2)
    while True:
        pos_cavalier.append(delta_cavalier)
        delta_cavalier = (-delta_cavalier[0], delta_cavalier[1])        
        pos_cavalier.append(delta_cavalier)
        delta_cavalier = (delta_cavalier[1], delta_cavalier[0])
        if delta_cavalier in pos_cavalier:
            for pos1 in pos_cavalier:
                pos2 = (pos1[0]+pos[0], pos1[1]+pos[1]) 
                if (pos_valide(liste, pos2) and (piece_pos(liste, pos2) == "." or 
                    piece_pos(liste, pos).isupper() and piece_pos(liste, pos2).islower() or
                    piece_pos(liste, pos).islower() and piece_pos(liste, pos2).isupper() )):
                    pos_cavalier2.append(pos2)
            return pos_cavalier2            

def pos_fou(liste, pos):
    pos_fou = []

    def test_fou(id_fou):
        if id_fou == 1: # test_fou(1)
            return (pos[0] + tour, pos[1] + tour)
        if id_fou == 2: # test_fou(2)
            return (pos[0] - tour , pos[1] + tour)
        
    # diagonale bas droite
    tour = 1
    while piece_pos(liste, test_fou(1)) == "." and pos_valide(liste, test_fou(1)):
        pos_fou.append(test_fou(1))
        tour += 1
    if pos_valide(liste, test_fou(1)):
        if ((piece_pos(liste, test_fou(1)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_fou(1)).islower() and piece_pos(liste, pos).isupper())):
            pos_fou.append(test_fou(1))    
    # diagonale haut gauche
    tour = -1
    while piece_pos(liste, test_fou(1)) == "." and pos_valide(liste, test_fou(1)): 
        pos_fou.append(test_fou(1))
        tour -= 1
    if pos_valide(liste, test_fou(1)):
        if ((piece_pos(liste, test_fou(1)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_fou(1)).islower() and piece_pos(liste, pos).isupper())):
            pos_fou.append(test_fou(1))
    
        # horizontale haute
    tour = 1
    while piece_pos(liste, test_fou(2)) == "." and pos_valide(liste, test_fou(2)):
        pos_fou.append(test_fou(2))
        tour += 1
    if pos_valide(liste, test_fou(2)):
        if ((piece_pos(liste, test_fou(2)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_fou(2)).islower() and piece_pos(liste, pos).isupper())):
            pos_fou.append(test_fou(2))    
    # horizontale basse
    tour = -1
    while piece_pos(liste, test_fou(2)) == "." and pos_valide(liste, test_fou(2)): 
        pos_fou.append(test_fou(2))
        tour -= 1
    if pos_valide(liste, test_fou(2)):
        if ((piece_pos(liste, test_fou(2)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_fou(2)).islower() and piece_pos(liste, pos).isupper())):
            pos_fou.append(test_fou(2))
    return pos_fou

def pos_tour(liste, pos):
    pos_tour = []

    def test_tour(id_tour):
        if id_tour == 1: # test_tour(1)
            return (pos[0] + tour, pos[1])
        if id_tour == 2: # test_tour(2)
            return (pos[0], pos[1] + tour)
        
    # verticale haute
    tour = 1
    while piece_pos(liste, test_tour(1)) == "." and pos_valide(liste, test_tour(1)):
        pos_tour.append(test_tour(1))
        tour += 1
    if pos_valide(liste, test_tour(1)):
        if ((piece_pos(liste, test_tour(1)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_tour(1)).islower() and piece_pos(liste, pos).isupper())):
            pos_tour.append(test_tour(1))    
    # verticale basse
    tour = -1
    while piece_pos(liste, test_tour(1)) == "." and pos_valide(liste, test_tour(1)): 
        pos_tour.append(test_tour(1))
        tour -= 1
    if pos_valide(liste, test_tour(1)):
        if ((piece_pos(liste, test_tour(1)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_tour(1)).islower() and piece_pos(liste, pos).isupper())):
            pos_tour.append(test_tour(1))
    
        # horizontale haute
    tour = 1
    while piece_pos(liste, test_tour(2)) == "." and pos_valide(liste, test_tour(2)):
        pos_tour.append(test_tour(2))
        tour += 1
    if pos_valide(liste, test_tour(2)):
        if ((piece_pos(liste, test_tour(2)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_tour(2)).islower() and piece_pos(liste, pos).isupper())):
            pos_tour.append(test_tour(2))    
    # horizontale basse
    tour = -1
    while piece_pos(liste, test_tour(2)) == "." and pos_valide(liste, test_tour(2)): 
        pos_tour.append(test_tour(2))
        tour -= 1
    if pos_valide(liste, test_tour(2)):
        if ((piece_pos(liste, test_tour(2)).isupper() and piece_pos(liste, pos).islower()) or 
            (piece_pos(liste, test_tour(2)).islower() and piece_pos(liste, pos).isupper())):
            pos_tour.append(test_tour(2))
    return pos_tour

def pos_dame(liste, pos):
    pos_dame = pos_fou(liste, pos) + pos_tour(liste, pos)
    return pos_dame

def pos_pion(liste, pos):
    pos_pion = []
    print(piece_pos(liste, pos))
    if piece_pos(liste, pos) == "P":
        if piece_pos(liste, (pos[0] + 1, pos[1])) == ".":
            pos_pion.append((pos[0] + 1, pos[1]))
        if piece_pos(liste, (pos[0] + 1, pos[1] + 1)).islower():
            pos_pion.append((pos[0] + 1, pos[1] + 1))
        if piece_pos(liste, (pos[0] + 1, pos[1] - 1 )).islower():
            pos_pion.append((pos[0] + 1, pos[1] - 1))
    if piece_pos(liste, pos) == "p":
        if piece_pos(liste, (pos[0] - 1, pos[1])) == ".":
            pos_pion.append((pos[0] - 1, pos[1]))
        if piece_pos(liste, (pos[0] - 1, pos[1] + 1)).isupper():
            pos_pion.append((pos[0] - 1, pos[1] + 1))
        if piece_pos(liste, (pos[0] - 1, pos[1] - 1 )).isupper():
            pos_pion.append((pos[0] - 1, pos[1] - 1))
    return pos_pion

def check_check(liste):
    for id_ligne in len(liste):
        for id_colonne in len(liste[0]):
            pos = (id_ligne, id_colonne)
            Rois = [] # {"R": (x, y)}
            if piece_pos(liste, pos) in "Rr":
                if piece_pos(liste, pos) == "R": Rois += {"R": (pos)}
                if piece_pos(liste, pos) == "r": Rois += {"r": (pos)}

def mouvement_valide(liste, mouvement):
    piece = piece_pos(liste, mouvement[0])
    if mouvement[0] == mouvement[1]:
        return False
    elif piece in "Pp":
        if mouvement[1] in pos_pion(liste, mouvement[0]):
            return True
    elif piece in "Cc": 
        if mouvement[1] in pos_cavalier(liste, mouvement[0]):
            return True
    elif piece in "Ff": 
        if mouvement[1] in pos_fou(liste, mouvement[0]):
            return True
    elif piece in "Tt":
        if mouvement[1] in pos_tour(liste, mouvement[0]):
            return True
    elif piece in "Dd": 
        if mouvement[1] in pos_dame(liste, mouvement[0]):
            return True
    return False

def mouvement_piece(liste, mouvement):
    if mouvement_valide(liste, mouvement):
        liste[mouvement[1][0]][mouvement[1][1]] = piece_pos(liste, mouvement[0])
        liste[mouvement[0][0]][mouvement[0][1]] = "."
    else:
        print("Mouvement " + str(mouvement) + " Invalide")
    return liste

def main():
    default_ligne_vide      = "........"
    default_ligne_piecesN   = "tcfdrfct"
    default_ligne_piecesB   = "tcfrdfct"
    default_ligne_pions     = "pppppppp"

    default_plateau = [ 
        [ [x] for x in default_ligne_piecesB.upper() ],
        [ [x] for x in default_ligne_pions.upper() ],
        [ [x] for x in default_ligne_vide ],  
        [ [x] for x in default_ligne_vide ],
        [ [x] for x in default_ligne_vide ],  
        [ [x] for x in default_ligne_vide ],
        [ [x] for x in default_ligne_pions ],
        [ [x] for x in default_ligne_piecesN ],
    ]

    test_plateau = [
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 0
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 1
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 2
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 3
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 4
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 5
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 6
         [["."],["."],["."],["."],["."],["."],["."],["."],], # 7
           #0    #1    #2    #3    #4    #5    #6    #7
    ]
    plateau = test_plateau

    actions_mouvements = [
       #((3, 3), (4, 3)),
    ]
    for id_mouvement in range(len(actions_mouvements)):
        plateau = mouvement_piece(plateau, actions_mouvements[id_mouvement])
        print_tableau(plateau)
        print("Tour: "+str(id_mouvement))
main()