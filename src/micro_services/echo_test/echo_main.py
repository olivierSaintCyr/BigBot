from flask import Flask
from flask_restful import Resource, Api, reqparse
import pymongo

app = Flask(__name__)
api = Api(app)

get_args_parser = reqparse.RequestParser()
get_args_parser.add_argument("_id", type=str, help="invalid server id")

mongo_client = pymongo.MongoClient("mongodb://database")
services_db = mongo_client["services"]
echoTest_data = services_db["echoTest"]

class EchoTest(Resource):
    def get(self):
        args = get_args_parser.parse_args()
        query = {"_id" : args['_id']}
        echo_data = echoTest_data.find(query)
        if echo_data.count() == 1:
            return {"data":echo_data[0]["phrase"]}
        else:
            return {"data":"Not setup properly"}

api.add_resource(EchoTest, '/')
if __name__=="__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
# TODO need to take info from database then send it back to the server

# TODO need to send it as json