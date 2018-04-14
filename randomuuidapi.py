from flask import Response
from flask_restful import Resource, reqparse, inputs
from uuid import uuid4
import string
import json

class RandomUUIDAPI(Resource):
    """Ransom UUID API"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('count', type=int, required=False)
        super(RandomUUIDAPI, self).__init__()

    def get(self):
        """Gets random UUID's"""
        args = self.reqparse.parse_args()
        # default params
        count = 1
        # Checks for optional params and reads them in
        if args.get('count'):
            count = args.get('count')
        # check for max values
        if count > 100:
            count = 100
        # list of numbers
        uuids = []
        # get the correct number of random numbers
        for i in range(0, count):
            uuids.append(uuid4().hex)
        # return numbers
        return Response(json.dumps(uuids),  mimetype='application/json')