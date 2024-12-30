# Blackjack-en-python
Jeu du Blackjack en python simplifié avec la *programmation orientée objet*.

# Comment jouer

Vous avez juste a telecharger le fichier `PythonBlackjack.py` et à l'ouvrir dans un IDE pour pouvoir l'executer et le programme fonctionnera tout simplement.  
Sinon avec python d'installer sur votre machine, vous n'avez qu'à juste vous placer dans le répertoire où se situe le fichier et faire :

```sh
python PythonBlackjack.py
```

# Présentation du programme

Le programme reprend d’une manière simplifiée, le jeu du Blackjack que l’on retrouve 
dans les casinos. Il est composé de 2 classes Cartes et Joueur ainsi que d’une
boucle principale pour le déroulement du jeu utilisant nos classes et fonctions.  

Le programme demande tout d’abord au joueur d’entrer une mise puis il affiche les 
mains du croupier et du joueur ainsi que le score du joueur et lui demande s’il veut 
continuer (piocher une nouvelle carte) ou s’arrêter.  

Si le joueur continue, il pioche une nouvelle carte. Selon son score on lui redemande 
s’il veut continuer mais s’il dépasse 21, la partie s’arrête puisqu’il a perdu. Son argent 
est mis à jour et on lui demande s’il veut rejouer.  

Si le joueur ne continue pas, on révèle la 2e carte du croupier et il pioche pour se 
rapprocher le plus possible de 21 comme le joueur.  

Si le joueur à un meilleur score que le croupier ou si le croupier dépasse 21, le joueur 
gagne et son argent est mis à jour.  

Si le joueur décide de rejouer, le jeu recommence en gardant son argent. Cependant 
si le joueur ne veut pas rejouer, le programme est arrêté et l’argent n’est pas gardé. 

# Choix des classes

* __Classe Carte__ :  
  La classe __Cartes__ sert à gérer la création d’un deck de 104 cartes mélangées. 
  La classe Cartes possède 3 attributs : un attribut `signes` qui représente un 
  tableau avec les signes possibles des cartes, un attribut `valeurs` qui 
  représente un tableau avec les valeurs possibles des cartes et un attribut 
  `deck` vide car le deck n’est pas encore créé.
  - La méthode `deck_melange` va créer un deck en utilisant nos attributs 
`signes` et `valeurs` et en les mettant dans un tuple sous la forme 
`(valeur, signe)` et les mettre dans un tableau. La méthode va ensuite 
doubler le deck pour en avoir un de 104 cartes puis elle va finalement le 
mélanger avec la fonction `shuffle` du module random.
  - La méthode `piocher` va piocher la dernière carte du deck en effectuant 
un `pop()` du deck qui est un tableau. On récupère le tuple du `pop()` et on le 
renvoi.

* __Classe Joueur__ :  
  La classe __Joueur__ sert à gérer les données du joueur. Elle possède les attributs 
suivants : `self.main` représente la main du joueur qui est un tableau vide, 
`self.argent` représente l’argent du joueur, `self.mise` représente la mise que le 
joueur va choisir et `self.score` représente le score qu’il a avec ses cartes pour 
pouvoir calculer une victoire ou une défaite.
  - La méthode `montant_mise` sert à mettre à jour la mise du joueur. Elle 
demande à l’utilisateur d’entrer une mise et vérifie que la mise est un 
nombre positif et inférieur ou égal à l’argent du joueur. Si la mise n’est pas 
valide, elle demande à nouveau à l’utilisateur d’entrer une mise.
  - La méthode `calcul_score` calcule le score total des cartes dans la main 
du joueur. Elle traite les As de manière spéciale : si le joueur à un As dans 
sa main, elle considère deux scores possibles (soit 1 pour l’As, soit 11), et 
choisit le score le plus élevé qui ne dépasse pas 21. Sinon elle convertit 
aussi les cartes figure comme le Roi en 10.
  - La méthode `calcul_defaite` et `calcul_victoire` mettent à jour l’argent 
du joueur selon qu’il perd ou qu’il gagne.

## Fonctions

La fonction `creation_deck` permet de créer un deck de carte. Elle instancie d’abord 
un nouvel objet de la classe __Cartes__, puis elle appelle la méthode `deck_melange` de 
cet objet pour créer et mélanger le paquet de cartes. Elle nous renvoi finalement le 
deck.  

La fonction `main_debut` est utilisée pour distribuer les cartes initiales au joueur et 
au croupier. Elle crée d’abord un nouvel objet croupier de la classe __Joueur__ et lui 
donne deux cartes du paquet. Ensuite, elle donne également deux cartes au joueur et 
calcule son score. Si le score du joueur est 21, elle annonce un “Blackjack”. Elle 
renvoie finalement les objets joueur et croupier.  

La fonction `main_croupier` est appelée lorsque le joueur décide de s’arrêter et de 
ne plus piocher de cartes. Elle révèle la main complète du croupier et calcule son 
score. Tant que le score du croupier est inférieur à celui du joueur, elle continue à 
tirer des cartes pour le croupier jusqu’à ce que son score soit supérieur ou égal à 
celui du joueur. 
