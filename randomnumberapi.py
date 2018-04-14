from flask import Response
from flask_restful import Resource, reqparse, inputs
from random import SystemRandom
import json


class RandomNumberAPI(Resource):
    """Ransom Number API"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('min', type=int, required=False)
        self.reqparse.add_argument('max', type=int, required=False)
        self.reqparse.add_argument('count', type=int, required=False)
        super(RandomNumberAPI, self).__init__()

    def get(self):
        """Gets random numbers"""
        args = self.reqparse.parse_args()
        # default params
        min = 0
        max = 100
        count = 1
        # Checks for optional params and reads them in
        if args.get('min'):
            min = args.get('min')
        if args.get('max'):
            max = args.get('max')
        if args.get('count'):
            count = args.get('count')
        # check for max values
        if count > 100:
            count = 100
        # list of numbers
        numbers = []
        # get the correct number of random numbers
        for i in range(0, count):
            numbers.append(SystemRandom().randint(min, max))
        # return numbers
        return Response(json.dumps(numbers),  mimetype='application/json')


