import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from tkcalendar import Calendar 

import datetime
from F_Gestion_Immeuble import (afficher_immeubles, ajouter_immeubles, ajouter_etages,
                               ajouter_appartements, ajouter_chambres, ajouter_locataire,
                               afficher_locataires, supprimer_locataire,cnx)


class GestionImmeubleApp:
    def __init__(self, master, cnx):
        self.master = master
        self.cnx = cnx  # Stocke cnx comme attribut de classe
        master.title("Gestion d'Immeuble")
        # Treeview pour afficher les données
        self.tree = ttk.Treeview(master, columns=("ID", "Nom", "Adresse"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Adresse", text="Adresse")
        self.tree.pack(pady=10)

        # Boutons pour chaque action
        self.btn_afficher_immeubles = tk.Button(master, text="Afficher les Immeubles", command=self.afficher_immeubles)
        self.btn_afficher_immeubles.pack(pady=10)

        self.btn_ajouter_immeubles = tk.Button(master, text="Ajouter des Immeubles", command=self.ajouter_immeubles)
        self.btn_ajouter_immeubles.pack(pady=10)

        self.btn_ajouter_etages = tk.Button(master, text="Ajouter des Étages", command=self.ajouter_etages)
        self.btn_ajouter_etages.pack(pady=10)

        self.btn_ajouter_appartements = tk.Button(master, text="Ajouter des Appartements", command=self.ajouter_appartements)
        self.btn_ajouter_appartements.pack(pady=10)

        self.btn_ajouter_chambres = tk.Button(master, text="Ajouter des Chambres", command=self.ajouter_chambres)
        self.btn_ajouter_chambres.pack(pady=10)

        self.btn_ajouter_locataire = tk.Button(root, text="Ajouter Locataire", command=self.ajouter_locataire)
        self.btn_ajouter_locataire.pack(pady=10)

        self.btn_afficher_locataires = tk.Button(master, text="Afficher Locataires", command=self.afficher_locataires)
        self.btn_afficher_locataires.pack(pady=10)

        self.btn_supprimer_locataire = tk.Button(master, text="Supprimer Locataire", command=self.supprimer_locataire)
        self.btn_supprimer_locataire.pack(pady=10)

        self.select_dates_button = tk.Button(master, text="Sélectionner les Dates", command=self.ajouter_locataire)
        self.select_dates_button.pack(pady=10)
        # Label et champ de saisie pour la date de début
        self.label_date_debut = tk.Label(master, text="Date de début (YYYY-MM-DD):")
        self.label_date_debut.pack(pady=5)
        self.entry_date_debut = tk.Entry(master)
        self.entry_date_debut.pack(pady=5)

        # Label et champ de saisie pour la date de fin
        self.label_date_fin = tk.Label(master, text="Date de fin (YYYY-MM-DD):")
        self.label_date_fin.pack(pady=5)
        self.entry_date_fin = tk.Entry(master)
        self.entry_date_fin.pack(pady=5)

        # Bouton pour valider les dates
        self.validate_button = tk.Button(master, text="Valider les Dates", command=self.ajouter_locataire)
        self.validate_button.pack(pady=10)
        
        self.btn_quitter = tk.Button(master, text="Quitter", command=master.quit)
        self.btn_quitter.pack(pady=10)

        self.tree = ttk.Treeview(root, columns=("ID", "Nom", "Prénom", "Téléphone", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prénom", text="Prénom")
        self.tree.heading("Téléphone", text="Téléphone")
        self.tree.heading("Email", text="Email")
        self.tree.pack(fill="both", expand=True)

        # Bouton pour ajouter un locataire
        self.btn_ajouter_locataire = tk.Button(root, text="Ajouter Locataire", command=self.ajouter_locataire)
        self.btn_ajouter_locataire.pack(pady=10)




    def afficher_immeubles(self):
        """Affiche les immeubles dans le Treeview."""
        try:
            immeubles = afficher_immeubles(self.cnx)  # Appel de la fonction qui retourne les immeubles
            #print("Immeubles récupérés:", immeubles)  # Affiche les résultats dans la console

            if immeubles is None or len(immeubles) == 0:
                messagebox.showerror("Erreur", "Aucun immeuble trouvé.")
                return

            # Vider l'ancien contenu du Treeview-
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insérer les données récupérées dans le Treeview
            for immeuble in immeubles:
                self.tree.insert("", "end", values=(immeuble[0], immeuble[1], immeuble[2]))  # ID, Nom, Adresse

        except Exception as e:
            messagebox.showerror("Erreur", str(e))




    def ajouter_immeubles(self):
        try:
            nombre_immeubles = simpledialog.askinteger("Ajouter Immeuble", "Combien d'immeubles voulez-vous saisir ?")
            for i in range(nombre_immeubles):
                nom = simpledialog.askstring("Nom Immeuble", f"Entrez le nom de l'immeuble {i + 1}:")
                adr = simpledialog.askstring("Adresse Immeuble", f"Entrez l'adresse de l'immeuble {i + 1}:")
                
                # Appeler la fonction ajouter_immeubles pour insérer les données dans la BDD
                ajouter_immeubles(self.cnx, nom, adr)

            messagebox.showinfo("Succès", "Immeubles ajoutés avec succès.")
            self.afficher_immeubles()  # Met à jour la liste affichée

        except Exception as e:
            messagebox.showerror("Erreur", str(e))



    def afficher_locataires(self):
        """Affiche les locataires dans le Treeview."""
        try:
            locataires = afficher_locataires(self.cnx)  # Passe self.cnx comme argument

            if locataires is None or len(locataires) == 0:
                messagebox.showerror("Erreur", "Aucun locataire trouvé.")
                return

            # Vider l'ancien contenu du Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Mise à jour des colonnes pour afficher les locataires
            self.tree["columns"] = ("ID", "Nom", "Prénom", "Téléphone", "Email", "Date Début", "Date Fin", "Loyer", "Contrat")
            self.tree.heading("ID", text="ID")
            self.tree.heading("Nom", text="Nom")
            self.tree.heading("Prénom", text="Prénom")
            self.tree.heading("Téléphone", text="Téléphone")
            self.tree.heading("Email", text="Email")
            self.tree.heading("Date Début", text="Date Début")
            self.tree.heading("Date Fin", text="Date Fin")
            self.tree.heading("Loyer", text="Loyer")
            self.tree.heading("Contrat", text="Contrat")

            # Insérer les données récupérées dans le Treeview
            for locataire in locataires:
                # `locataire` est un tuple, inséré directement dans le Treeview
                self.tree.insert("", "end", values=locataire)

        except Exception as e:
            messagebox.showerror("Erreur", str(e))


    def ajouter_etages(self):
            try:
                ajouter_etages(self.cnx)  # Passe self.cnx comme argument
                messagebox.showinfo("Succès", "Étages ajoutés avec succès.")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

    def ajouter_appartements(self):
        try:
            ajouter_appartements(self.cnx)  # Passe self.cnx comme argument
            messagebox.showinfo("Succès", "Appartements ajoutés avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def ajouter_chambres(self):
        try:
            ajouter_chambres(self.cnx)  # Passe self.cnx comme argument
            messagebox.showinfo("Succès", "Chambres ajoutés avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
        # Création d'un Treeview pour afficher les locataires

    def ajouter_locataire(self):
        cursorSel = None
        cursorInsert = None
        try:
            # Étape 1 : Sélectionner l'immeuble
            cursorSel = self.cnx.cursor()
            selectImmeuble = "SELECT id_immeuble, nom, adresse FROM immeuble"
            cursorSel.execute(selectImmeuble)
            immeubles = cursorSel.fetchall()
            
            immeuble_options = [f"{immeuble[1]} - {immeuble[2]}" for immeuble in immeubles]
            choix_immeuble = simpledialog.askinteger("Choix de l'immeuble", "Entrez le numéro de l'immeuble\n" + "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(immeuble_options)))
            
            if choix_immeuble is None or choix_immeuble < 1 or choix_immeuble > len(immeubles):
                messagebox.showerror("Erreur", "Choix d'immeuble invalide.")
                return
            
            id_immeuble = immeubles[choix_immeuble - 1][0]
            nom_immeuble = immeubles[choix_immeuble - 1][1]

            # Étape 2 : Sélectionner le type de bien
            choix_bien = simpledialog.askstring("Type de Bien", "Le locataire veut-il un appartement ou une chambre ? (a/c) :").lower()

            if choix_bien == 'a':
                # Sélection d'un appartement
                selectAppartement = """
                    SELECT id_appartement, surface_m2, nombre_chambre
                    FROM appartement 
                    WHERE Etage_id_etage IN (SELECT id_etage FROM etage WHERE Immeuble_id_immeuble = %s)
                """
                cursorSel.execute(selectAppartement, (id_immeuble,))
                appartements = cursorSel.fetchall()
                
                appartement_options = [f"Appartement {app[0]} - Surface: {app[1]}m², Chambres: {app[2]}" for app in appartements]
                choix_appartement = simpledialog.askinteger("Choix Appartement", "Choisissez un appartement\n" + "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(appartement_options)))
                
                if choix_appartement is None or choix_appartement < 1 or choix_appartement > len(appartements):
                    messagebox.showerror("Erreur", "Choix d'appartement invalide.")
                    return
                
                id_bien = appartements[choix_appartement - 1][0]

            elif choix_bien == 'c':
                # Sélection d'une chambre
                selectChambre = """
                    SELECT id_chambre, surface_m2 
                    FROM chambre 
                    WHERE Appartement_id_appartement IN (
                        SELECT id_appartement FROM appartement 
                        WHERE Etage_id_etage IN (SELECT id_etage FROM etage WHERE Immeuble_id_immeuble = %s)
                    )
                """
                cursorSel.execute(selectChambre, (id_immeuble,))
                chambres = cursorSel.fetchall()

                chambre_options = [f"Chambre {ch[0]} - Surface: {ch[1]}m²" for ch in chambres]
                choix_chambre = simpledialog.askinteger("Choix Chambre", "Choisissez une chambre\n" + "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(chambre_options)))
                
                if choix_chambre is None or choix_chambre < 1 or choix_chambre > len(chambres):
                    messagebox.showerror("Erreur", "Choix de chambre invalide.")
                    return
                
                id_bien = chambres[choix_chambre - 1][0]
            else:
                messagebox.showerror("Erreur", "Choix de bien invalide.")
                return

            # Étape 3 : Saisie des informations du locataire

                # Étape 3 : Saisie des informations du locataire
            nom_locataire = simpledialog.askstring("Nom", "Entrez le nom du locataire :")
            prenom_locataire = simpledialog.askstring("Prénom", "Entrez le prénom du locataire :")
            telephone = simpledialog.askstring("Téléphone", "Entrez le numéro de téléphone :")
            email = simpledialog.askstring("Email", "Entrez l'email :")
            date_debut = simpledialog.askstring("Date début", "Entrez la date de début du contrat (AAAA-MM-JJ) :")
            date_fin = simpledialog.askstring("Date fin", "Entrez la date de fin du contrat (AAAA-MM-JJ) :")
            loyer = simpledialog.askfloat("Loyer", "Entrez le montant du loyer :")
            contrat = simpledialog.askstring("Contrat", "Entrez les informations du contrat :")

            # Vérification des champs obligatoires
            if not all([nom_locataire, prenom_locataire, telephone, email, date_debut, date_fin, loyer, contrat]):
                messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
                return

            # Insertion du locataire dans la base de données
            cursorInsert = self.cnx.cursor()
            add_locataire = """
                INSERT INTO locataire (nom, prenom, telephone, email, date_debut, date_fin, montant_loyer, libelle_contrat)
                VALUES (%(nom)s, %(prenom)s, %(telephone)s, %(email)s, %(date_debut)s, %(date_fin)s, %(loyer)s, %(contrat)s)
            """
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
            cursorInsert.execute(add_locataire, data_locataire)
            id_locataire = cursorInsert.lastrowid

            # Mise à jour du bien avec le locataire
            update_bien = (
                "UPDATE appartement SET Locataire_id_locataire = %s WHERE id_appartement = %s"
                if choix_bien == 'a' else
                "UPDATE chambre SET Locataire_id_locataire = %s WHERE id_chambre = %s"
            )
            cursorInsert.execute(update_bien, (id_locataire, id_bien))

            # Confirmer l'ajout
            self.cnx.commit()
            messagebox.showinfo("Succès", f"Le locataire {nom_locataire} {prenom_locataire} a été ajouté.")
        
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur SQL", f"Erreur lors de l'ajout du locataire : {err}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inattendue : {e}")
        finally:
            # Fermer les curseurs s'ils existent
            if cursorSel is not None:
                cursorSel.close()
            if cursorInsert is not None:
                cursorInsert.close()


    def supprimer_locataire(self):
        try:
            locataire_id = simpledialog.askinteger("Supprimer Locataire", "Entrez l'ID du locataire à supprimer :")
            if locataire_id is not None:
                supprimer_locataire(self.cnx, locataire_id)  # Passe self.cnx comme argument
                messagebox.showinfo("Succès", f"Locataire avec l'ID {locataire_id} a été supprimé.")
                self.afficher_locataires()  # Met à jour la liste des locataires affichée
            else:
                messagebox.showwarning("Annulé", "Aucune action effectuée.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

if __name__ == "__main__":
    import mysql.connector
    from mysql.connector import errorcode

    # Configuration de la connexion à la base de données
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

    root = tk.Tk()
    app = GestionImmeubleApp(root, cnx)  # Passe cnx ici
    root.mainloop()

    # Fermer la connexion à la base de données lorsque l'application se ferme
    cnx.close()
