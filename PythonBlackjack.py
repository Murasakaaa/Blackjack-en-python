import random
import time

class Cartes:

    def __init__(self):
        self.signes = ['Coeur', 'Pique', 'Trèfle', 'Carreau']
        self.valeurs = ['As', "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi"]
        self.deck = []

    def deck_melange(self):
        """Crée un paquet de 104 cartes, une carte est représentée par un tuple contenant sa
        valeur et son signe. Puis les cartes sont mélangées."""
        for valeur in self.valeurs:
            for signe in self.signes:
                self.deck.append((valeur, signe))
        self.deck = self.deck * 2
        random.shuffle(self.deck)   # mélange le deck
        return self.deck

    """def piocher(self):
      pioche la dernière carte du deck prédédemment crée
        carte = self.deck.pop()     # récupère la carte piochée
        return carte"""

class Joueur:

    def __init__(self):
        self.main = []
        self.argent = 0
        self.mise = 0
        self.score = 0

    def montant_mise(self):
        """défini le montant de la mise du joueur"""
        while True:
            try:
                self.mise = int(input(f"Votre mise ? (1-{self.argent}): "))
                if self.mise <= 0:
                    print("vous devez mettre une mise")
                    continue
                if self.mise > self.argent:
                    print("Vous n'avez pas assez d'argent")
                    continue
            except ValueError:
                print("Veuillez remettre une mise correcte")
                continue
            else:
                break

    def calcul_score(self, main):
        """permet de calculer le score total des cartes de notre mains"""
        min = 0
        max = 0
        as_present = False          # False car on a pas encore d'As
        for carte in main:
            if carte[0] == "As" and as_present is True:     # un As est déjà present donc on prend la valeur
                min += 1                                    # la plus intéressante pour le joueur
                max += 1
            elif carte[0] == "As" and as_present is False:
                as_present = True       # On a maintenant un As donc True
                min += 1
                max += 11
            elif carte[0] == "Valet" or carte[0] == "Reine" or carte[0] == "Roi":  # on converti les figures en 10
                min += 10
                max += 10
            elif int(carte[0]) in range(2, 11):     # on converti les cartes simples
                min += int(carte[0])
                max += int(carte[0])
        # on va prendre la valeur la plus proche de 21 sans dépasser entre min et max
        if max == min:
            score = min
        elif max <= 21:
            score = max
        elif max > 21:
            score = min
        return score

    def calcul_defaite(self, a):
        self.argent = self.argent-a
        return self.argent

    def calcul_victoire(self, a):
        self.argent += a*1.5
        return self.argent

def creation_deck():
    c = Cartes()
    d = c.deck_melange()
    print("taille du deck: ", len(d))
    return d

def main_debut(joueur1, deck):
    """distribue les cartes du début"""
    croupier = Joueur()
    croupier.main = [deck.pop(), deck.pop()]
    time.sleep(1)
    # On montre seulement 1 carte car l'autre est cachée
    print(f"Main du croupier: ['{croupier.main[0]}', '????']")
    # On a les 2 cartes du début de la main du joueur
    joueur1.main = [deck.pop(), deck.pop()]
    joueur1.score = joueur1.calcul_score(joueur1.main)
    time.sleep(1)
    print(f"Main du Joueur: {joueur1.main}")
    print(f"score du Joueur: {joueur1.score}")
    if joueur1.score == 21:
        print("Blackjack!")
    return joueur1, croupier

def main_croupier():
    """fonction lorsque le joueur decide de s'arrêter, on revele donc la carte du croupier"""
    time.sleep(1)
    print(f'main du croupier{croupier.main}')
    croupier.score = croupier.calcul_score(croupier.main)
    # si le score du croupier est plus petit que celui du joueur il repioche une carte
    while croupier.score < joueur.score:
        time.sleep(1)
        new_croupier_card = deck.pop()
        croupier.main.append(new_croupier_card)
        print(f'main du croupier{croupier.main}')
        croupier.score = croupier.calcul_score(croupier.main)
    print(f"Score du croupier: {croupier.score}")
    print(f"Votre score: {joueur.score}")

def rejouer():
    """demande au joueur si il veut rejouer"""

jeu_actif = True
argent = 50
# deroulement du jeu
while jeu_actif is True:
    deck = creation_deck()
    joueur = Joueur()
    joueur.argent = argent
    print(f'votre argent: {joueur.argent}$')
    if joueur.argent == 0:
        print("Vous n'avez plus d'argent")
        jeu_actif = False
        break
    else:
        joueur.montant_mise()
    time.sleep(1)
    joueur, croupier = main_debut(joueur, deck)
    time.sleep(1)
    continuer = ""
    while continuer != "non":
        continuer = input("entrer 'oui' si vous voulez avoir une autre carte sinon entrer 'non': ")
        if continuer == "oui":  # le joueur veut continuer
            print("Le joueur demande une autre carte")
            time.sleep(1)
            # on rajoute une carte au Joueur
            joueur.main.append(deck.pop())
            print(f"Joueur: {joueur.main}")
            # calcul du nouveau score
            joueur.score = joueur.calcul_score(joueur.main)
            print(f"Score: {joueur.score}")
            # si le joueur dépasse 21, il a perdu
            if joueur.score > 21:
                print("Perdu !")
                print(f"La mise était de: {joueur.mise}$")
                argent = int(joueur.calcul_defaite(joueur.mise))
                print(f"Argent: {joueur.argent}$")
                time.sleep(1)
                print("Nouvelle partie")
                o = input("voulez vous rejouer ? (oui/non): ")
                if o == 'non':
                    jeu_actif = False
                break
            elif joueur.score == 21:
                print("Blackjack!")
                print("Vous avez gagnez !")
                argent = int(joueur.calcul_victoire(joueur.mise))
                print(f"Argent: {joueur.argent}$")
                time.sleep(1)
                o = input("voulez vous rejouer ? (oui/non): ")
                if o == 'non':
                        jeu_actif = False
                        break

        elif continuer == "non":
            # Le joueur s'arrête et on revele donc la 2eme carte du croupier
            # On regarde ensuite qui gagne
            print("Le joueur ne demande pas d'autre cartes")
            time.sleep(1)
            main_croupier()
            if croupier.score > joueur.score and croupier.score <= 21:

                print("Vous avez perdu!")
                argent = int(joueur.calcul_defaite(joueur.mise))
                print(f"Argent: {joueur.argent}$")
                time.sleep(1)
            elif croupier.score == joueur.score:
                print("égalité !")
                time.sleep(1)
            else:
                print("Vous avez gagnez !")
                argent = int(joueur.calcul_victoire(joueur.mise))
                print(f"Argent: {joueur.argent}$")
                time.sleep(1)
            o = input("voulez vous rejouer ? (oui/non): ")
            if o == 'non':
                jeu_actif = False
                break
            print("Nouvelle partie")
            time.sleep(1)

'''
Blackjack:
déroulement du jeu:
- une carte visible pour le joueur
- une carte visible pour le croupier
- une carte visible pour le joueur
- une carte cachée pour le croupier

-> si le joueur a Blackjack, cest fini, il a gagné

-> si le joueur n'a pas Blackjack:
- soit il demande une autre carte pour tenter d'être le plus proche de 21 (il peu avoir jusqu'a 4 cartes)
- soit il s'arrête et attend le résultat

 >21 perd dans tous les cas
 blackjack = victoire (égalité si le croupier aussi)
 sinon si le joueur à plus de valeur que le croupier il gagne
'''