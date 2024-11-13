import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

######################################
#### Configurer la BDD SQLite #####
####################################
# récupérer le répertoire
basedir = os.path.abspath(os.path.dirname(__file__))
#__file__: représente le fichier actuel
#os.path.dirname(__file__) renvoie le chemin du répertoire parent du fichier en cours d'exécution. 
#os.path.abspath(os.path.dirname(__file__)) renvoie le chemin absolu du répertoire 
# contenant le fichier actuel, indépendamment de l'endroit où le script est exécuté.

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)


#########################################
### Créer les colonnes de la tables ####
########################################

class User(db.Model):
    __tablename__ = 'users'
    # Clé primaire, id de chaque user
    id = db.Column(db.Integer, primary_key=True)
    # nom_user de 64 caractères au max, unique (sans doublons) 
    # Créer un index sur la colonne pour optimiser les performances 
    # lors de la recherche et du filtrage des données basées sur cette colonne. 
    nom_user = db.Column(db.String(64), unique=True, index=True)
    #Mot de passe de 128 caractères au maximum
    mdp = db.Column(db.String(128))

    # id sera automatiquement créer, on ne l'ajoute pas au constructeur!
    def __init__(self, nom, mdp):
        self.nom_user = nom
        self.mdp =  mdp
             
    def __repr__(self):
        # renvoie une chaine de représentation d'un user
        return f"User:  {self.nom_user}"
        
  