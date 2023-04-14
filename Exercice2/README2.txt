I )


Le but de cette exercie est d'implémenter l'algorithme minmax et de les tester sur un exemple concret. On choisit de les tester sur l'exemple du morpion qui est un exemple que tout le monde connait.

minmax.py est un exemple de code en pyton qui implémente l'algorithme minmax sur l'exemple du morpion et affiche la grille de départ et celle aprés decision.
Pour le lancer on tape la ligne de commande : python3 minmax.py

L'algorithme Minimax peut être utilisé pour jouer à des jeux de décision comme le Tic-Tac-Toe (ou Morpion). Dans ce genre de jeux, l'algorithme Minimax permet de trouver le meilleur mouvement à faire en analysant toutes les possibilités de jeu jusqu'à la fin du jeu.




Pour utiliser l'algorithme Minimax pour jouer au Tic-Tac-Toe, on doit d'abord définir l'arbre de jeu, qui représente toutes les possibilités de jeu à chaque étape. Chaque nœud de l'arbre représente un état de jeu (c'est-à-dire, une grille de Tic-Tac-Toe avec les pions déjà joués) et chaque enfant d'un nœud représente un mouvement possible à partir de cet état.

Voici comment implémenter l'algorithme Minimax pour jouer au Tic-Tac-Toe :

 1 - Définir la classe TreeNode pour représenter un nœud de l'arbre de jeu. Chaque nœud a un état de jeu (c'est-à-dire, une grille de Tic-Tac-Toe avec les pions déjà joués) et peut avoir des enfants (qui sont eux-mêmes des nœuds).
 
 2 - Définir la fonction minimax qui parcourt l'arbre de jeu en utilisant la récursion. À chaque nœud, la fonction calcule le score de l'état de jeu en fonction de si le joueur MAX (le joueur qui joue les croix) ou le joueur MIN (le joueur qui joue les ronds) a gagné, perdu ou fait match nul. Si la profondeur de recherche est atteinte ou si le nœud n'a pas d'enfants, la fonction renvoie le score de l'état de jeu du nœud. Sinon, elle parcourt tous les enfants du nœud et calcule le score de chacun d'entre eux en utilisant récursivement la fonction minimax. Ensuite, elle utilise ces scores pour déterminer le meilleur mouvement à faire à partir de l'état actuel.
 
3 - Création l'arbre de jeu à partir de l'état de départ du jeu (une grille vide de Tic-Tac-Toe).
    
Ensuite on appelle la fonction minimax en lui passant la racine de l'arbre de jeu, la profondeur de recherche souhaitée et le joueur qui doit jouer
 


II ) 

Le but de cette exercie est d'implémenter les algorithme minmax et alphabeta et de les tester sur un exemple concret. On choisit de les tester sur l'exemple du morpion (Tic Tac Toe ) qui est un exemple que tout le monde connait.

alphabeta.py est un exemple de code en pyton qui implémente l'algorithme alphabeta sur l'exemple du morpion et sort la valeur optimal.
Pour le lancer on tape la ligne de commande : python3 alphabeta.py

Pour implémenter l'algorithme alpha/beta sur une structure d'arbre, on peut utiliser la même structure de code que pour l'algorithme minmax, en ajoutant simplement les paramètres alpha et beta et en utilisant ces paramètres pour mettre à jour l'intervalle de valeurs possibles en fonction de l'état de la partie.
