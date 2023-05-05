from flask import Flask,request
from flask_restful import Resource,Api
import math

app = Flask(__name__)
api = Api(app)


class GCD(Resource):
    def get(self,x,y):
        n1 = float(x)
        n2 = float(y)
        while(n2):
            n1, n2 = n2, n1 % n2
        return n1
        


api.add_resource(GCD,'/gcd/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5057)