from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

# Create the application instance
app = Flask(__name__, template_folder="template")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('devise') #ajout de la variable de la devise de paiement
parser.add_argument('distance') #ajout de la variable de la distance du trajet

prix_km = 1.2 #prix moyen au km pour un trajet en ter en 2em classe https://ressources.data.sncf.com/explore/dataset/bareme-de-prix-national-ter/table/?sort=-km

@app.route('/')
def home():
    return render_template('index.html') #fichier contenu dans le repertoire template/


# Calcul du prix en fonction de la distance et de l'unité passé dans l'URL
class Calcul_Prix(Resource):
    def get(self):
        args = parser.parse_args()
        if args['devise'] == 'Euro':
            prix = float(args['distance']) * prix_km
            return prix
        #Franc Suisse
        elif args['devise'] == 'CHF':
            prix = float(args['distance']) * prix_km * 1.05
            return prix
        elif args['devise'] == 'YEN':
            prix = float(args['distance']) * prix_km * 116.702
            return prix
        #Couronne Danoise
        elif args['devise'] == 'DKK':
            prix = float(args['distance']) * prix_km * 7.46
            return prix
        #Couronne Suedoise
        elif args['devise'] == 'SKK':
            prix = float(args['distance']) * prix_km * 10.86
            return prix


api.add_resource(Calcul_Prix, '/Calcul_Prix')