import database as db
from departements.departement import Departement

class DepartementDao:
    # Établir une connexion à la base de données
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, dpt: Departement):
        """
        Insérer un nouveau département dans la base de données.

        :param dpt: L'objet département à insérer
        :return: Un message de succès ou d'erreur
        """
        sql = "INSERT INTO departement (nom, emplacement, direction) VALUES (%s, %s, %s)"
        params = (dpt.nom, dpt.emplacement, dpt.direction)

        try:
            DepartementDao.cursor.execute(sql, params)
            DepartementDao.connexion.commit()
            message = "Succès"
        except Exception as exc:
            message = "Erreur"

        return message

    @classmethod
    def list_all(cls):
        """
        Récupérer tous les départements de la base de données.

        :return: Une liste de tous les départements
        """
        sql = "SELECT * FROM departement"
        DepartementDao.cursor.execute(sql)
        Departements = DepartementDao.cursor.fetchall()

        return Departements

    @classmethod
    def delete(cls, id):
        """
        Supprimer un département de la base de données en utilisant son ID.

        :param id: L'ID du département à supprimer
        """
        sql = "DELETE FROM departement WHERE id=%s"
        DepartementDao.cursor.execute(sql, (id,))
        DepartementDao.connexion.commit()

        print(f"Suppression du département avec l'id : {id}.")

    @classmethod
    def update(cls, id, dpt: Departement):
        """
        Mettre à jour les informations d'un département dans la base de données en utilisant son ID.

        :param id: L'ID du département à mettre à jour
        :param dpt: L'objet département mis à jour
        """
        sql = "UPDATE departement SET nom=%s, emplacement=%s, direction=%s WHERE id=%s"
        params = (dpt.nom, dpt.emplacement, dpt.direction, id)
        DepartementDao.cursor.execute(sql, params)
        DepartementDao.connexion.commit()

        print(f"Département : {dpt.nom} est mis à jour.")
