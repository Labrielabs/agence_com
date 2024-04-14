from utilisateur_dao import UtilisateurDao

(message,utilisateur)= UtilisateurDao.get_one('','')

print(message,utilisateur)