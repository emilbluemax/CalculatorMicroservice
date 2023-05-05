from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class EqualTo(Resource):
    def get(self,x,y):
        x = float(x)
        y = float(y)
        if x == y:
            return True
        else:
            return False

api.add_resource(EqualTo,'/equalto/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5055)