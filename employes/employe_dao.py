import database as db
from employes.Employe import Employe

class EmployeDao:
    # Établir une connexion à la base de données
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    @classmethod
    def get_all(cls):
        # Définir la requête SQL pour récupérer tous les employés
        sql = "SELECT * FROM employe"
        # Exécuter la requête SQL
        EmployeDao.cursor.execute(sql)
        # Récupérer toutes les lignes retournées par la requête
        employes = EmployeDao.cursor.fetchall()
        # Retourner la liste des employés
        return employes

    @classmethod
    def add(cls, emp: Employe):
        # Définir la requête SQL pour insérer un nouvel employé
        sql = "INSERT INTO employe (nom, prenom, matricule, fonction, departement) VALUES (%s, %s, %s, %s, %s)"
        # Définir les paramètres pour la requête SQL
        params = (emp.nom, emp.prenom, emp.matricule, emp.fonction, emp.departement)
        try:
            # Exécuter la requête SQL avec les paramètres donnés
            EmployeDao.cursor.execute(sql, params)
            # Valider les changements dans la base de données
            EmployeDao.connexion.commit()
            # Définir le message de succès
            message = "Success"
        except Exception as ex:
            # Définir le message d'erreur
            message = "Error"
        # Retourner le message
        return message

    @classmethod
    def get_one(cls, matricule):
        # Définir la requête SQL pour récupérer un employé spécifique par son matricule
        sql = "SELECT * FROM employe WHERE matricule=%s"
        try:
            # Exécuter la requête SQL avec le matricule donné
            EmployeDao.cursor.execute(sql, (matricule,))
            # Définir le message de succès
            message = "Succès"
            # Récupérer la première ligne retournée par la requête
            employe = EmployeDao.cursor.fetchone()
        except Exception as ex:
            # Définir le message d'erreur
            message = "Erreur pendant la recherche"
            # Définir l'employé à une liste vide
            employe = []
        # Retourner le message et l'employé
        return (message, employe)
