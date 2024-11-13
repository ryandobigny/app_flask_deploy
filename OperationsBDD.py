
#Ceci est un script très simple qui  montrera comment configurer la BDD
#Plus tard, on utilisera ce code avec des templates#

#############################################################################
#NOTE !! Si vous exécutez ce script plusieurs fois, vous ajouterez
#plusieurs users et roles  à la base de données. C'est correct, seulement les
# dentifiants seront supérieurs à 1, 2 lors des exécutions suivantes
#########################################################################

#Importer les informations de la base de données
from ModeleDeBDD import db, User, app

#est une méthode dans Flask qui crée un objet de contexte d'application.
# Ce contexte permet d'accéder aux variables liées à l'application qui
# sont normalement accessibles uniquement pendant une requête HTTP.
#current_appcurrent_app est une variable de contexte qui pointe vers 
# l'application Flask actuellement active. En dehors d'un contexte de requête 
# ou d'application, current_app n'a pas de sens et son accès lèvera une exception
# car Flask ne sait pas à quelle application se référer.
# À l'intérieur d'un contexte d'application créé par app.app_context(), 
# current_app est automatiquement défini pour référencer l'instance 
# de l'application Flask correcte: current_app.config['SECRET_KEY'])  


if __name__ == "__main__":            
    with app.app_context():
        # Créer les tables dans la BDD
        db.drop_all()
        db.create_all()
        john = User('John',"admin") 
        susan = User('Susan', "mdp@123") 
        david = User('David', "dav80!")
            
        #ajouter les objets à la session: ids vont être créés automatiquement
        db.session.add(john)
        db.session.add(susan)
        db.session.add(david)
        #Une alternative à l'ajout alternatif
        #db.session.add_all([admin_role,mod_role,user_role,john,susan,david])

        #insérer les objets en BDD
        db.session.commit() 
        print("Users ajoutés")
        
        print(f"Avant mise à jour : {john.mdp}")
        john.mdp = "confidentiel"
        db.session.commit()
        print(f"Après mise à jour : {john.mdp}")

        '''print(f"Existence de David avant suppression : {david in db.session}")
        db.session.delete(david)
        db.session.commit()
        print(f"Existence de David après suppression : {david in db.session}")
        '''
        all_users = User.query.all()
        for user in all_users:
            print(user)
        print(f"User N°1", User.query.first())
        print(f"User N°2", User.query.get(2))
        print(f"Total: {User.query.count()}")
        print(User.query.filter_by(mdp="dav80!").first())
        print(User.query.filter(User.nom_user=="John").first())
        print(User.query.filter(User.nom_user.like('%dav%')).all())
        
        # Trouver tous les utilisateurs dont le nom est soit "John" soit "Susan"
        users = User.query.filter(User.nom_user.in_(['John', 'Susan'])).all()
        print(users)
        # Trouver tous les utilisateurs sauf "John" et "Susan"
        users = User.query.filter(~User.nom_user.in_(['John', 'Susan'])).all()
        print(users)
        
        magda = User('Magda', None)
        db.session.add(magda)
        db.session.commit()
        print(f"ID: {magda.id}, {magda}")
        users_a_pwd_null = User.query.filter(User.mdp == None).all()
        print(users_a_pwd_null)
        #Trouver tous les utilisateurs dont le mot de passe n'est pas NULL
        users_a_pwd = User.query.filter(User.mdp != None).all()
        print(users_a_pwd)
        
        user = User.query.filter(db.and_(User.nom_user == "John", User.mdp == "confidentiel")).first()
        print(user)
        user = User.query.filter(User.nom_user == "John").filter(User.mdp == "secret").first()
        print(user)
        user = User.query.filter(User.nom_user == "John", User.mdp == "confidentiel").first()
        print(user)
        users = User.query.filter(db.or_(User.nom_user == "John", User.mdp == "dav80!")).all()
        print(users)
        
        users = User.query.order_by(User.nom_user).all()
        print(users)
        # Trier les utilisateurs par nom d'utilisateur en ordre décroissant
        users = User.query.order_by(User.nom_user.desc()).all()
        print(users)
        print(User.query.order_by(User.nom_user).limit(3).all())
        print(User.query.all())
        print(User.query.offset(2).all())
        print(User.query.offset(2).limit(3).all())
        print(User.query.filter(User.id >= 2).all())
        
    app.run(debug=True, port="5003")

                    
   






