from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Modulus(Resource):
    def get(self,x,y):
        if(float(y) == 0):
            return "2nd number CANT be ZERO"
        return float(x)%float(y)

api.add_resource(Modulus,'/modulus/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5061)