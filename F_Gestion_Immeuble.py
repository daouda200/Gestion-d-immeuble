import mysql.connector
import pandas as pd
from mysql.connector import errorcode
from tkinter import messagebox

# Connexion à la base de données
config = {
    'user': 'root',
    'password': 'daouda',
    'host': '127.0.0.1',
    'database': 'Gestion_Immeuble',
    'raise_on_warnings': True
}

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("L'utilisateur ou le mot de passe n'est pas correct")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas")
    else:
        print("Erreur non gérée:", err)
    exit()

# Sélection des informations

def afficher_immeubles(cnx):
    cursorSel = cnx.cursor()
    selectAction = ("SELECT * FROM immeuble")
    cursorSel.execute(selectAction)
    resultSelect = cursorSel.fetchall()
    for i in resultSelect:
        print(f"ID: {i[0]}, Nom: {i[1]}, adresse: {i[2]}")
    cursorSel.close()
    return resultSelect 




'''
def ajouter_immeubles(cnx):
    nombre_immeubles = int(input("Combien d'immeubles voulez-vous saisir ? "))
    for i in range(nombre_immeubles):
        nom = str(input(f"Entrez le nom de l'immeuble {i + 1}: "))
        adr = str(input(f"Entrez l'adresse de l'immeuble {i + 1}: "))
        data_immeuble = {
            'nomimm': nom,
            'adresseim': adr,
        }
        cursorInsert = cnx.cursor()
        add_immeuble = (
            "INSERT INTO immeuble (nom, adresse) "
            "VALUES (%(nomimm)s, %(adresseim)s)"
        )
        cursorInsert.execute(add_immeuble, data_immeuble)
        cnx.commit()
        print(cursorInsert.rowcount, f"Immeuble {i + 1} inséré(e)s")
        cursorInsert.close()
'''

def ajouter_immeubles(cnx, nom, adr):
    try:
        cursorInsert = cnx.cursor()
        add_immeuble = (
            "INSERT INTO immeuble (nom, adresse) "
            "VALUES (%s, %s)"
        )
        cursorInsert.execute(add_immeuble, (nom, adr))
        cnx.commit()
        cursorInsert.close()
        print(f"Immeuble ajouté: {nom}, {adr}")

    except Exception as e:
        print(f"Erreur lors de l'ajout de l'immeuble: {str(e)}")




def ajouter_etages(cnx):
    print("Liste des immeubles disponibles:")
    cursorSel = cnx.cursor()
    selectImmeuble = "SELECT id_immeuble, nom, adresse FROM immeuble"
    cursorSel.execute(selectImmeuble)
    immeubles = cursorSel.fetchall()
    for idx, immeuble in enumerate(immeubles):
        print(f"{idx + 1}. Nom: {immeuble[1]}, Adresse: {immeuble[2]}")
    choix = int(input("Choisissez un immeuble par son numéro : ")) - 1
    if choix < 0 or choix >= len(immeubles):
        print("Choix invalide !")
    else:
        id_immeuble = immeubles[choix][0]
        nom_immeuble = immeubles[choix][1]
        adresse_immeuble = immeubles[choix][2]
        print(f"Vous avez choisi l'immeuble '{nom_immeuble}' à l'adresse '{adresse_immeuble}'.")
        nombre_etages = int(input(f"Combien d'étages voulez-vous ajouter à '{nom_immeuble}' ? "))
        for i in range(nombre_etages):
            num_etage = input(f"Saisissez le numéro de l'étage {i + 1}: ")
            data_etage = {
                'num_etage': num_etage,
                'id_immeuble': id_immeuble
            }
            cursorInsert = cnx.cursor()
            add_etage = (
                "INSERT INTO etage (numeroetage, Immeuble_id_immeuble) "
                "VALUES (%(num_etage)s, %(id_immeuble)s)"
            )
            cursorInsert.execute(add_etage, data_etage)
            cnx.commit()
            print(f"Étage {num_etage} ajouté à l'immeuble '{nom_immeuble}'.")
            cursorInsert.close()

def ajouter_appartements(cnx):
    print("Liste des immeubles disponibles:")
    cursorSel = cnx.cursor()
    selectImmeuble = "SELECT id_immeuble, nom, adresse FROM immeuble"
    cursorSel.execute(selectImmeuble)
    immeubles = cursorSel.fetchall()
    for idx, immeuble in enumerate(immeubles):
        print(f"{idx + 1}. Nom: {immeuble[1]}, Adresse: {immeuble[2]}")
    choix = int(input("Choisissez un immeuble par son numéro : ")) - 1
    if choix < 0 or choix >= len(immeubles):
        print("Choix invalide !")
    else:
        id_immeuble = immeubles[choix][0]
        nom_immeuble = immeubles[choix][1]
        adresse_immeuble = immeubles[choix][2]
        print(f"Vous avez choisi l'immeuble '{nom_immeuble}' à l'adresse '{adresse_immeuble}'.")
        print(f"Affichage des étages de l'immeuble '{nom_immeuble}' :")
        selectEtage = "SELECT id_etage, numeroetage FROM etage WHERE Immeuble_id_immeuble = %s"
        cursorSel.execute(selectEtage, (id_immeuble,))
        etages = cursorSel.fetchall()
        if len(etages) == 0:
            print("Aucun étage trouvé pour cet immeuble.")
        else:
            for idx, etage in enumerate(etages):
                print(f"{idx + 1}. Numéro Étages: {etage[1]}")
            choix_etage = int(input("Choisissez un étage par son numéro : ")) - 1
            if choix_etage < 0 or choix_etage >= len(etages):
                print("Choix invalide !")
            else:
                id_etage = etages[choix_etage][0]
                numero_etage = etages[choix_etage][1]
                print(f"Vous avez choisi l'étage numéro {numero_etage}.")
                num_appartement = input("Saisissez le numéro de l'appartement : ")
                surface_appartement = float(input("Saisissez la surface de l'appartement (en m²) : "))
                nb_chambres = int(input("Saisissez le nombre de chambres : "))
                id_locataire = input("Saisissez l'ID du locataire (ou laissez vide si aucun locataire) : ")
                id_locataire = id_locataire if id_locataire else None
                data_appartement = {
                    'numero_appartement': num_appartement,
                    'surface_appartement': surface_appartement,
                    'nb_chambres': nb_chambres,
                    'id_etage': id_etage                }
                cursorInsert = cnx.cursor()
                add_appartement = (
                    "INSERT INTO appartement (numero_appartement, surface_m2, nombre_chambre, Etage_id_etage) "
                    "VALUES (%(numero_appartement)s, %(surface_appartement)s, %(nb_chambres)s, %(id_etage)s)"
                )
                cursorInsert.execute(add_appartement, data_appartement)
                cnx.commit()
                print(f"Appartement numéro {num_appartement} ajouté à l'étage {numero_etage} de l'immeuble '{nom_immeuble}'.")


def ajouter_chambres(cnx):
    print("Liste des immeubles disponibles:")
    cursorSel = cnx.cursor()
    selectImmeuble = "SELECT id_immeuble, nom, adresse FROM immeuble"
    cursorSel.execute(selectImmeuble)
    immeubles = cursorSel.fetchall()
    for idx, immeuble in enumerate(immeubles):
        print(f"{idx + 1}. Nom: {immeuble[1]}, Adresse: {immeuble[2]}")
    choix = int(input("Choisissez un immeuble par son numéro : ")) - 1
    if choix < 0 or choix >= len(immeubles):
        print("Choix invalide !")
    else:
        id_immeuble = immeubles[choix][0]
        nom_immeuble = immeubles[choix][1]
        adresse_immeuble = immeubles[choix][2]
        print(f"Vous avez choisi l'immeuble '{nom_immeuble}' à l'adresse '{adresse_immeuble}'.")
        print(f"Affichage des étages de l'immeuble '{nom_immeuble}' :")
        selectEtage = "SELECT id_etage, numeroetage FROM etage WHERE Immeuble_id_immeuble = %s"
        cursorSel.execute(selectEtage, (id_immeuble,))
        etages = cursorSel.fetchall()
        if len(etages) == 0:
            print("Aucun étage trouvé pour cet immeuble.")
        else:
            for idx, etage in enumerate(etages):
                print(f"{idx + 1}. Numéro Étages: {etage[1]}")
            choix_etage = int(input("Choisissez un étage par son numéro : ")) - 1
            if choix_etage < 0 or choix_etage >= len(etages):
                print("Choix invalide !")
            else:
                id_etage = etages[choix_etage][0]
                numero_etage = etages[choix_etage][1]
                print(f"Vous avez choisi l'étage numéro {numero_etage}.")
                print(f"Affichage des appartements de l'étage numéro {numero_etage} :")
                selectAppartement = """
                    SELECT id_appartement, numero_appartement, surface_m2, nombre_chambre
                    FROM appartement
                    WHERE Etage_id_etage = %s
                """
                cursorSel.execute(selectAppartement, (id_etage,))
                appartements = cursorSel.fetchall()
                if len(appartements) == 0:
                    print("Aucun appartement trouvé pour cet étage.")
                else:
                    for idx, appartement in enumerate(appartements):
                        print(f"{idx + 1}. Numéro Appartement: {appartement[1]}, Surface: {appartement[2]} m², Chambres: {appartement[3]}")
                    choix_appartement = int(input("Choisissez un appartement par son numéro : ")) - 1
                    if choix_appartement < 0 or choix_appartement >= len(appartements):
                        print("Choix invalide !")
                    else:
                        id_appartement = appartements[choix_appartement][0]
                        numero_appartement = appartements[choix_appartement][1]
                        print(f"Vous avez choisi l'appartement numéro {numero_appartement}.")
                        num_chambre = input("Saisissez le numéro de la chambre : ")
                        surface_chambre = float(input("Saisissez la surface de la chambre (en m²) : "))
                        id_locataire = input("Saisissez l'ID du locataire (ou laissez vide si aucun locataire) : ")
                        id_locataire = id_locataire if id_locataire else None
                        data_chambre = {
                            'numero_chambre': num_chambre,
                            'surface_chambre': surface_chambre,
                            'id_appartement': id_appartement,
                            'id_locataire': id_locataire
                        }
                        cursorInsert = cnx.cursor()
                        add_chambre = (
                            "INSERT INTO chambre (numero_chambre, surface_m2, Appartement_id_appartement, Locataire_id_locataire) "
                            "VALUES (%(numero_chambre)s, %(surface_chambre)s, %(id_appartement)s, %(id_locataire)s)"
                        )
                        cursorInsert.execute(add_chambre, data_chambre)
                        cnx.commit()
                        print(f"Chambre numéro {num_chambre} ajoutée à l'appartement numéro {numero_appartement} de l'immeuble '{nom_immeuble}', étage {numero_etage}.")

def ajouter_locataire(cnx):
    # Étape 1: Récupérer tous les immeubles disponibles pour les afficher sous forme de menu
    print("Liste des immeubles disponibles:")
    
    cursorSel = cnx.cursor()
    selectImmeuble = "SELECT id_immeuble, nom, adresse FROM immeuble"
    
    try:
        cursorSel.execute(selectImmeuble)
        immeubles = cursorSel.fetchall()
    except mysql.connector.Error as err:
        print("Erreur de requête SQL:", err)
        return
    
    # Afficher les immeubles sous forme de menu
    for idx, immeuble in enumerate(immeubles):
        print(f"{idx + 1}. Nom: {immeuble[1]}, Adresse: {immeuble[2]}")
    
    # Étape 2: Demander à l'utilisateur de choisir un immeuble
    choix = int(input("Choisissez un immeuble par son numéro : ")) - 1
    
    if choix < 0 or choix >= len(immeubles):
        print("Choix invalide !")
        return
    
    # Récupérer la clé primaire de l'immeuble sélectionné
    id_immeuble = immeubles[choix][0]
    nom_immeuble = immeubles[choix][1]
    adresse_immeuble = immeubles[choix][2]
    
    print(f"Vous avez choisi l'immeuble '{nom_immeuble}' à l'adresse '{adresse_immeuble}'.")
    
    # Étape 3: Demander si le locataire veut un appartement ou une chambre
    choix_bien = input("Le locataire veut-il un appartement ou une chambre ? (a/c) : ").lower()
    
    if choix_bien == 'a':
        # Choix appartement
        print(f"Affichage des appartements de l'immeuble '{nom_immeuble}' :")
        
        selectAppartement = """
            SELECT a.*
            FROM appartement a
            INNER JOIN etage e ON a.Etage_id_etage = e.id_etage
            WHERE e.Immeuble_id_immeuble= %s
        """
        try:
            cursorSel.execute(selectAppartement, (id_immeuble,))
            appartements = cursorSel.fetchall()
        except mysql.connector.Error as err:
            print("Erreur de requête SQL:", err)
            return
        
        # Afficher les appartements sous forme de menu
        for idx, appartement in enumerate(appartements):
            print(f"{idx + 1}. Numéro Appartement: {appartement[1]}, Surface: {appartement[2]} m², Chambres: {appartement[3]}, Etage_id : {appartement[4]},locataire_id : {appartement[5]}")
        
        # Choisir un appartement
        choix_appartement = int(input("Choisissez un appartement par son numéro : ")) - 1
        
        if choix_appartement < 0 or choix_appartement >= len(appartements):
            print("Choix invalide !")
            return
        
        id_appartement = appartements[choix_appartement][0]
        numero_appartement = appartements[choix_appartement][1]
        
        print(f"Vous avez choisi l'appartement numéro {numero_appartement}.")
        
        # Étape 4: Saisie des informations du locataire
        nom_locataire = input("Saisissez le nom du locataire : ")
        prenom_locataire = input("Saisissez le prénom du locataire : ")
        telephone = input("Saisissez le numéro de téléphone : ")
        email = input("Saisissez l'email : ")
        date_debut = input("Saisissez la date de début du contrat (AAAA-MM-JJ) : ")
        date_fin = input("Saisissez la date de fin du contrat (AAAA-MM-JJ) : ")
        loyer = float(input("Saisissez le montant du loyer : "))
        contrat = input("Saisissez les informations du contrat : ")
        
        # Création du dictionnaire avec les données du locataire
        data_locataire = {
            'nom': nom_locataire,
            'prenom': prenom_locataire,
            'telephone': telephone,
            'email': email,
            'date_debut': date_debut,
            'date_fin': date_fin,
            'loyer': loyer,
            'contrat': contrat
        }
        
        # Insertion du locataire dans la base de données
        cursorInsert = cnx.cursor()
        
        add_locataire = """
            INSERT INTO locataire (nom, prenom, telephone, email, date_debut, date_fin, montant_loyer, libelle_contrat)
            VALUES (%(nom)s, %(prenom)s, %(telephone)s, %(email)s, %(date_debut)s, %(date_fin)s, %(loyer)s, %(contrat)s)
        """
        try:
            cursorInsert.execute(add_locataire, data_locataire)
            id_locataire = cursorInsert.lastrowid
        except mysql.connector.Error as err:
            print("Erreur d'insertion du locataire:", err)
            return
        
        # Mettre à jour l'appartement pour y lier le locataire
        update_appartement = "UPDATE appartement SET Locataire_id_locataire = %s WHERE id_appartement = %s"
        try:
            cursorInsert.execute(update_appartement, (id_locataire, id_appartement))
        except mysql.connector.Error as err:
            print("Erreur de mise à jour de l'appartement:", err)
            return
        
        # Confirmer l'insertion
        cnx.commit()
        
        print(f"Le locataire {nom_locataire} {prenom_locataire} a été assigné à l'appartement numéro {numero_appartement}.")
    
    elif choix_bien == 'c':
        # Choix chambre
        print(f"Affichage des chambres de l'immeuble '{nom_immeuble}' :")
        
        selectChambre = """
            SELECT c.*
            FROM chambre c
            INNER JOIN appartement a ON c.Appartement_id_appartement = a.id_appartement
            INNER JOIN etage e ON a.Etage_id_etage = e.id_etage
            WHERE e.Immeuble_id_immeuble = %s
        """
        try:
            cursorSel.execute(selectChambre, (id_immeuble,))
            chambres = cursorSel.fetchall()
        except mysql.connector.Error as err:
            print("Erreur de requête SQL:", err)
            return
        
        # Afficher les chambres sous forme de menu
        for idx, chambre in enumerate(chambres):
            print(f"{idx + 1}. Numéro Chambre: {chambre[1]}, Surface: {chambre[2]} m², Appartement: {chambre[3]}, Etage: {chambre[4]}")
        
        # Choisir une chambre
        choix_chambre = int(input("Choisissez une chambre par son numéro : ")) - 1
        
        if choix_chambre < 0 or choix_chambre >= len(chambres):
            print("Choix invalide !")
            return
        
        id_chambre = chambres[choix_chambre][0]
        numero_chambre = chambres[choix_chambre][1]
        
        print(f"Vous avez choisi la chambre numéro {numero_chambre}.")
        
        # Étape 4: Saisie des informations du locataire
        nom_locataire = input("Saisissez le nom du locataire : ")
        prenom_locataire = input("Saisissez le prénom du locataire : ")
        telephone = input("Saisissez le numéro de téléphone : ")
        email = input("Saisissez l'email : ")
        date_debut = input("Saisissez la date de début du contrat (AAAA-MM-JJ) : ")
        date_fin = input("Saisissez la date de fin du contrat (AAAA-MM-JJ) : ")
        loyer = float(input("Saisissez le montant du loyer : "))
        contrat = input("Saisissez les informations du contrat : ")
        
        # Création du dictionnaire avec les données du locataire
        data_locataire = {
            'nom': nom_locataire,
            'prenom': prenom_locataire,
            'telephone': telephone,
            'email': email,
            'date_debut': date_debut,
            'date_fin': date_fin,
            'loyer': loyer,
            'contrat': contrat
        }
        
        # Insertion du locataire dans la base de données
        cursorInsert = cnx.cursor()
        
        add_locataire = """
            INSERT INTO locataire (nom, prenom, telephone, email, date_debut, date_fin, montant_loyer, libelle_contrat)
            VALUES (%(nom)s, %(prenom)s, %(telephone)s, %(email)s, %(date_debut)s, %(date_fin)s, %(loyer)s, %(contrat)s)
        """
        try:
            cursorInsert.execute(add_locataire, data_locataire)
            id_locataire = cursorInsert.lastrowid
        except mysql.connector.Error as err:
            print("Erreur d'insertion du locataire:", err)
            return
        
        # Mettre à jour la chambre pour y lier le locataire
        update_chambre = "UPDATE chambre SET Locataire_id_locataire = %s WHERE id_chambre = %s"
        try:
            cursorInsert.execute(update_chambre, (id_locataire, id_chambre))
        except mysql.connector.Error as err:
            print("Erreur de mise à jour de la chambre:", err)
            return
        
        # Confirmer l'insertion
        cnx.commit()
        
        print(f"Le locataire {nom_locataire} {prenom_locataire} a été assigné à la chambre numéro {numero_chambre}.")
    
    else:
        print("Choix invalide pour le type de bien.")
    
    cursorSel.close()
    cursorInsert.close()

'''
def afficher_locataires(cnx):
    cursorSel = cnx.cursor()
    selectLocataire = "SELECT * FROM locataire"
    cursorSel.execute(selectLocataire)
    locataires = cursorSel.fetchall()

    # Créer un DataFrame à partir des résultats
    df = pd.DataFrame(locataires, columns=['ID', 'Nom', 'Prénom', 'Téléphone', 'Email', 'Date Début', 'Date Fin', 'Loyer', 'Contrat'])

    # Afficher le DataFrame
    print(df)

    cursorSel.close()
    return df
'''

def afficher_locataires(cnx):
    cursorSel = cnx.cursor()
    selectLocataire = "SELECT * FROM locataire"
    cursorSel.execute(selectLocataire)
    locataires = cursorSel.fetchall()

    # Retourner les locataires sous forme de liste de tuples, pas besoin de DataFrame ici
    cursorSel.close()
    return locataires  # Retourne directement les locataires sans créer de DataFrame


def supprimer_locataire(cnx):
    # Appel de la fonction afficher_locataires pour récupérer les locataires
    df = afficher_locataires(cnx)

    # Demander à l'utilisateur de choisir un locataire à supprimer
    try:
        locataire_id = int(input("Entrez l'ID du locataire que vous voulez supprimer : "))
        
        # Vérifier si l'ID existe dans le DataFrame
        if locataire_id in df['ID'].values:
            # Étape 1 : Mettre à jour la table 'chambre' pour dé-référencer le locataire
            cursorUpdate = cnx.cursor()
            updateChambre = "UPDATE chambre SET Locataire_id_locataire = NULL WHERE Locataire_id_locataire = %s"
            cursorUpdate.execute(updateChambre, (locataire_id,))
            
            # Étape 2 : Mettre à jour la table 'appartement' pour dé-référencer le locataire
            updateAppartement = "UPDATE appartement SET Locataire_id_locataire = NULL WHERE Locataire_id_locataire = %s"
            cursorUpdate.execute(updateAppartement, (locataire_id,))
            cnx.commit()

            # Étape 3 : Supprimer le locataire
            deleteQuery = "DELETE FROM locataire WHERE id_locataire = %s"
            cursorDelete = cnx.cursor()
            cursorDelete.execute(deleteQuery, (locataire_id,))
            cnx.commit()

            print(f"Le locataire avec l'ID {locataire_id} a été supprimé.")
            
            cursorUpdate.close()
            cursorDelete.close()
        else:
            print("ID non trouvé dans la liste des locataires.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre valide pour l'ID.")
'''

def menu_principal():
    while True:
        print("Menu principal")
        print("1. Afficher les immeubles")
        print("2. Ajouter des immeubles")
        print("3. Ajouter des étages")
        print("4. Ajouter des appartements")
        print("5. Ajouter des chambres")
        print("6. Ajouter locataires")
        print("7. afficher locataire")
        print("8. supprimer locataire")
        print("9. Quitter")
        choix = input("Choisissez une option : ")
        if choix == "1":
            afficher_immeubles(cnx)
        elif choix == "2":
            ajouter_immeubles(cnx)
        elif choix == "3":
            ajouter_etages(cnx)
        elif choix == "4":
            ajouter_appartements(cnx)
        elif choix == "5":
            ajouter_chambres(cnx)
        elif choix == "6":
            ajouter_locataire(cnx)  
        elif choix == "7":
            afficher_locataires(cnx)  
        elif choix == "8":    
            supprimer_locataire(cnx)        
        elif choix == "9":
            print("Au revoir !")
            break
        else:
            print("Choix invalide !")

menu_principal()'''