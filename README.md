# Bot Discord - Jeu de Mots

Ce bot Discord permet aux utilisateurs de jouer à un jeu où ils ajoutent des mots à une base de données et accumulent des points. Le bot vérifie si les mots sont valides (présents dans un dictionnaire français) et les ajoute à la base de données avec un score pour chaque utilisateur.

## Fonctionnalités

- **Ajouter un mot** : Les utilisateurs peuvent ajouter des mots au jeu. Si le mot est valide, il est ajouté à la base de données et l'utilisateur gagne un point.
- **Afficher les mots** : Les utilisateurs peuvent afficher tous les mots ajoutés au jeu avec leurs auteurs.
- **Afficher les scores** : Le bot affiche le score de chaque utilisateur en fonction du nombre de mots qu'ils ont ajoutés.
- **Supprimer tous les mots** : Les administrateurs peuvent supprimer tous les mots de la base de données à l'aide de la commande `!clear`.
- **Maintien du bot en ligne** : Le bot reste en ligne grâce à la fonction `keep_alive()`.
