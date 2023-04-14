Pour lancer le noeud et le master : roslaunch surveillance_system surveillance.launch


Le programme est un nœud ROS qui s'abonne aux messages du drone et de trois robots (R1, R2 et R3). Il définit des fonctions de callback pour chacune de ces sources de messages.

Lorsque le drone publie un message, la fonction de callback drone_callback est appelée. Cette fonction convertit le message en un entier et vérifie s'il n'est pas égal à 0. Si le message n'est pas égal à 0, la fonction appelle la fonction choose_site_to_verify pour choisir l'un des sites à vérifier. La fonction définit alors le bit correspondant au site choisi sur 0 dans le message et publie le message modifié au robot 1.

Lorsque le robot 1 publie un message, la fonction de callback robot1_callback est appelée. Cette fonction convertit le message en un entier et vérifie s'il n'est pas égal à 0. Si le message n'est pas égal à 0, la fonction appelle la fonction choose_site_to_verify pour choisir l'un des sites restants à vérifier. La fonction définit alors le bit correspondant au site choisi sur 0 dans le message et publie le message modifié au robot 2.

Les fonctions de callback robot2_callback et robot3_callback fonctionnent de manière similaire, avec le robot 2 qui publie au robot 3 et le robot 3 ne prenant aucune autre action. Si le message reçu par l'un des robots est égal à 0, les robots n'effectuent aucune action.

Le but du programme est de permettre au drone de publier des messages indiquant quels sites doivent être vérifiés et pour que les robots choisissent et vérifient ces sites de manière séquentielle. Le programme utilise le système de messagerie éditeur-abonné ROS pour communiquer entre le drone et les robots.


 / ! \ Pour l'instant on choisit la zone à verifier aléatoirement mais dans un cadre dévelopement industrielle il serait bon de préferait la zone la plus proche du robot !
