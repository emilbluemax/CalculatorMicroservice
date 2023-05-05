from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Division(Resource):
    def get(self,x,y):
        x = float(x)
        y = float(y)
        if y==0:
            return "Division by zero is INVALID"
        return x/y

api.add_resource(Division,'/div/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5054)
