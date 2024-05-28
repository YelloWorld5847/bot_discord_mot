import sqlite3


def initialiser_db():
    conn = sqlite3.connect('jeu_mot.db')
    cur = conn.cursor()

    # Créer une table pour les mots
    cur.execute('''
        CREATE TABLE IF NOT EXISTS jeu_mot (
            id INTEGER PRIMARY KEY,
            utilisateur TEXT NOT NULL,
            mot TEXT NOT NULL UNIQUE
        )
    ''')

    # Créer une table pour les utilisateurs
    cur.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            nom TEXT PRIMARY KEY,
            score INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# Fonction pour ajouter un mot
# Fonction pour ajouter un mot et mettre à jour le score
def ajouter_mot(utilisateur, mot):
    conn = sqlite3.connect('jeu_mot.db')
    cur = conn.cursor()

    # Vérifier si le mot existe déjà
    cur.execute('SELECT * FROM jeu_mot WHERE mot = ?', (mot,))
    row = cur.fetchone()

    if row:
        conn.close()
        return True
    else:
        # Ajouter le mot à la base de données
        cur.execute('INSERT INTO jeu_mot (utilisateur, mot) VALUES (?, ?)', (utilisateur, mot))

        # Mettre à jour le score de l'utilisateur
        cur.execute('SELECT * FROM utilisateurs WHERE nom = ?', (utilisateur,))
        user_row = cur.fetchone()

        if user_row:
            # Utilisateur existe, mettre à jour le score
            cur.execute('UPDATE utilisateurs SET score = score + 1 WHERE nom = ?', (utilisateur,))
        else:
            # Nouvel utilisateur, insérer dans la table
            cur.execute('INSERT INTO utilisateurs (nom, score) VALUES (?, ?)', (utilisateur, 1))

        conn.commit()
        conn.close()
        return True




# Fonction pour afficher tous les mots et leurs utilisateurs
def afficher_mots():
    # Établir une connexion à la base de données
    conn = sqlite3.connect('jeu_mot.db')
    # Créer un curseur
    cur = conn.cursor()

    cur.execute('SELECT utilisateur, mot FROM jeu_mot')
    rows = cur.fetchall()

    mots = []
    if rows:
        for row in rows:
            mots.append(f"Utilisateur : {row[0]}, Mot : {row[1]}")
    else:
        mots.append("Aucun mot trouvé dans la base de données.")

    # Fermer la connexion
    conn.close()
    return '\n'.join(mots)


# Fonction pour afficher le score de tous les utilisateurs
def afficher_scores():
    conn = sqlite3.connect('jeu_mot.db')
    cur = conn.cursor()

    cur.execute('SELECT nom, score FROM utilisateurs ORDER BY score DESC')
    rows = cur.fetchall()

    scores = []
    if rows:
        for row in rows:
            scores.append(f"Utilisateur : {row[0]}, Score : {row[1]}")
    else:
        scores.append("Aucun utilisateur trouvé dans la base de données.")

    conn.close()
    return '\n'.join(scores)


def clear_tables():
    # Connexion à la base de données
    conn = sqlite3.connect('jeu_mot.db')
    cur = conn.cursor()

    # Supprimer tous les éléments de la table
    cur.execute('DELETE FROM jeu_mot')

    # Valider les changements
    conn.commit()
    # Fermer la connexion
    conn.close()


def scan_dict(mot_test):
    with open('dict.txt', 'r') as file:
        mots = [mot.strip() for mot in file.readlines()]


    if mot_test in mots:
        return True
    else:
        return False