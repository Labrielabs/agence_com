import database as db
import flask_bcrypt as bcrypt
from utilisateurs.utilisateur import Utilisateur

class UtilisateurDao:
    # Initialiser la connexion à la base de données et le curseur
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, utl: Utilisateur):
        """
        Créer un nouvel utilisateur dans la base de données.

        :param utl: L'objet utilisateur à créer.
        :return: Un message indiquant le succès ou l'échec.
        """
        sql = "INSERT INTO utilisateurs (nom, username, mdp) VALUES (%s, %s, %s)"
        params = (utl.nom, utl.username, utl.mdp)
        try:
            UtilisateurDao.cursor.execute(sql, params)
            UtilisateurDao.connexion.commit()
            message = "Success"
        except Exception as exc:
            message = "Error"
        return message
    
    @classmethod
    def list_all(cls):
        """
        Récupérer tous les utilisateurs de la base de données.

        :return: Une liste de tous les utilisateurs.
        """
        sql = "SELECT * FROM utilisateurs"
        UtilisateurDao.cursor.execute(sql)
        utilisateurs = UtilisateurDao.cursor.fetchall()
        
        return utilisateurs
    
    @classmethod
    def get_one(cls, username, mdp):
        """
        Récupérer un seul utilisateur de la base de données par nom d'utilisateur et mot de passe.

        :param username: Le nom d'utilisateur de l'utilisateur à récupérer.
        :param mdp: Le mot de passe de l'utilisateur à récupérer.
        :return: Un tuple contenant un message et l'objet utilisateur.
        """
        sql = "SELECT * FROM utilisateurs WHERE username=%s"
        try:
            UtilisateurDao.cursor.execute(sql, (username,))
            utilisateur = UtilisateurDao.cursor.fetchone()
            if utilisateur:
                if bcrypt.check_password_hash(utilisateur[3], mdp):
                    message = "Succès"
        except Exception as ex:
            message = "Erreur"
            utilisateur = []
        return (message, utilisateur)
