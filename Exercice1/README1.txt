Formalisation du problème:

Etats: L'état du système peut être représenté par la position de chaque robot sur la grille. Par exemple, si les robots sont situés aux positions (2,3), (4,2) et (1,1) sur la grille, l'état peut être représenté par la triplette (2,3,4,2,1,1).

Actions: Les actions disponibles pour chaque robot peuvent être déplacer le robot vers un emplacement adjacent (haut, bas, gauche, droite) ou le laisser à sa position actuelle.

Fonctions heuristiques: Une fonction heuristique possible est la distance de Manhattan entre la position actuelle du robot et sa destination finale. Cette fonction heuristique permet de sous-estimer la distance réelle entre la position actuelle et la destination finale, ce qui est nécessaire pour que l'algorithme A* fonctionne correctement.



astar.py est un exemple de code en pyton qui implémente l'algorithme de planification à base de A* pour trouver un plan joint pour les trois robots sur la grille donnée

Ce code affichera la grille à chaque étape de la planification par robot ( le 1 puis le 2 puis le 3) avec remanence de la trace du robot, avec chaque robot représenté par un numéro différent (1, 2 ou 3).


Pour le lancer on tape la ligne de commande : python3 astar.py
