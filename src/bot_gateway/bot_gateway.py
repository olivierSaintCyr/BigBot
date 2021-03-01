# TODO need to support every microservices and send back the request to bot
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
import json
import pymongo

app = Flask(__name__)
api = Api(app)

get_args_parser = reqparse.RequestParser()
get_args_parser.add_argument("server_id", type=str, help="invalid server id argument")
get_args_parser.add_argument("service", type=str, help="invalid service argument")

mongo_client = pymongo.MongoClient("mongodb://database")
services_db = mongo_client["services"]
guild_services_col = services_db["guild_services"]

class BotGateway(Resource):
    def get(self):
        args = get_args_parser.parse_args()

        query = {"_id":args["server_id"]}
        guild_services = guild_services_col.find(query)

        if guild_services.count() == 1:
            services = guild_services[0]['services']

            if args['service'] in services:
                service_query = {"_id":args["server_id"]}
                service_url = "http://" + args['service']
                response = requests.get(service_url, service_query)
                return response.json(), response.status_code
            else:
                return "This server is not subscribed to this service", 200
        else:
            return "The server is not setup", 200

api.add_resource(BotGateway, '/')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)