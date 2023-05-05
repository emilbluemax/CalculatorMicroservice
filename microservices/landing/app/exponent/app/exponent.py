from flask import Flask,request
from flask_restful import Resource,Api
import math

app = Flask(__name__)
api = Api(app)


class Exponent(Resource):
    def get(self,x,y):
        n1 = float(x)
        n2 = float(y)
        return math.pow(n1,n2)

api.add_resource(Exponent,'/exponent/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5056)