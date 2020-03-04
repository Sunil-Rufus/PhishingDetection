from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Observatory(Resource):
    def get(self):
       data = {'message': 'Its good url'}
       return data ,200

api.add_resource(Observatory, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
