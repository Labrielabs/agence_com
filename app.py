from flask import Flask, render_template, url_for, request, session, redirect
from flask_bcrypt import Bcrypt

# Importation des classes et modules nécessaires pour la gestion des Employés et des Départements
from employes.Employe import Employe
from employes.employe_dao import EmployeDao
from departements.departement import Departement
from departements.departement_dao import DepartementDao

# Importation des classes et modules nécessaires pour la gestion des Utilisateurs
from utilisateurs.utilisateur import Utilisateur
from utilisateurs.utilisateur_dao import UtilisateurDao

# Initialisation de l'application Flask et définition d'une clé secrète pour la gestion des sessions
app = Flask(__name__)
app.secret_key = "jesuislemaitredesclefs"

# Initialisation de l'objet Bcrypt pour le hachage des mots de passe
bcrypt = Bcrypt(app)

# Route pour la page d'accueil
@app.route("/")
def home():
    return render_template("index.html")

# Route pour la page À propos
@app.route("/about")
def about():
    return render_template("about.html")

# Route pour la page Services
@app.route("/services")
def services():
    return render_template("services.html")

# Route pour l'inscription des utilisateurs
@app.route("/register", methods=["GET", "POST"])
def register():
    message = None
    utilisateur = None

    # Récupération des données du formulaire à partir de la requête
    req = request.form

    if request.method == "POST":
        nom = req["nom"]
        username = req["username"]
        mdp = req["mdp"]

        # Hachage du mot de passe avec Bcrypt
        hashed_password = bcrypt.generate_password_hash(mdp).decode("utf-8")

        if nom == "" or username == "" or mdp == "":
            message = "Erreur"
        else:
            # Création d'un nouvel objet Utilisateur avec les données du formulaire
            utilisateur = Utilisateur(nom, username, hashed_password)

            # Tentative de création du nouvel Utilisateur dans la base de données
            message = UtilisateurDao.create(utilisateur)

    # Rendu du template register avec les variables message et utilisateur
    return render_template(f"register.html", message=message, utilisateur=utilisateur)

@app.route("/login", methods=["GET", "POST"])
def login():
    req = request.form
    message = "Veuillez entrer vos identifiants."  # Message par défaut
    utilisateur = None

    if request.method == "POST":
        username = req.get("username", "")
        mdp = req.get("mdp", "")

        if not username or not mdp:
            message = "Tous les champs sont obligatoires."
        else:
            try:
                # Récupération de l'utilisateur
                message, utilisateur = UtilisateurDao.get_one(username, mdp)
                if message == "Succès" and utilisateur:
                    if bcrypt.check_password_hash(utilisateur[3], mdp):
                        session["username"] = utilisateur[2]
                        session["nom"] = utilisateur[1]
                        return redirect(url_for("home"))
                    else:
                        message = "Nom d'utilisateur ou mot de passe incorrect."
            except Exception as ex:
                message = f"Erreur lors de la connexion: {str(ex)}"

    return render_template("login.html", message=message, utilisateur=utilisateur)


# Route pour la déconnexion des utilisateurs
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/departements")
def departements():
    departements = DepartementDao.list_all()
    return render_template("departements.html", departements=departements)

@app.route("/add-departements",methods=["POST","GET"])
def add_departements():
    req = request.form
    message = None
    departement = None
    if request.method == "POST":
        nom = req['nom']
        emplacement = req['emplacement']
        direction = req['direction']
        if nom=="" or emplacement=="" or direction=="":
            message="Erreur"
        else:
            departement = Departement(nom,emplacement,direction)
            message = DepartementDao.create(departement)
    return render_template("add_departements.html",message=message,departement=departement)



# Route pour afficher tous les employés
@app.route("/employe")
def employes():
    if "username" not in session:
        return redirect(url_for("login"))

    # Récupération de tous les employés depuis la base de données
    employes = EmployeDao.get_all()

    # Rendu du template employe avec la variable employes
    return render_template("employe.html", employes=employes)

# Route pour ajouter un nouvel employé
@app.route("/add-employe", methods=["POST", "GET"])
def add_employe():
    if "username" not in session:
        return redirect(url_for("login"))

    req = request.form
    message = None
    employe = None

    if request.method == "POST":
        nom = req["nom"]
        prenom = req["prenom"]
        matricule = req["matricule"]
        fonction = req["fonction"]
        departement = req["departement"]

        if nom == "" or prenom == "" or matricule == "" or fonction == "" or departement == "":
            message = "Erreur"
        else:
            # Création d'un nouvel objet Employe avec les données du formulaire
            employe = Employe(nom, prenom, matricule, fonction, departement)

            # Tentative d'ajout du nouvel Employe dans la base de données
            message = EmployeDao.add(employe)

    # Rendu du template add_employe avec les variables employe et message
    return render_template("add_employe.html", employe=employe, message=message)



