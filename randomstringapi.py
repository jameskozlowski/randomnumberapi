from flask import Response
from flask_restful import Resource, reqparse, inputs
from random import SystemRandom, choice
import string
import json

class RandomStringAPI(Resource):
    """Ransom String API"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('min', type=int, required=False)
        self.reqparse.add_argument('max', type=int, required=False)
        self.reqparse.add_argument('count', type=int, required=False)
        self.reqparse.add_argument('all', type=inputs.boolean , required=False)
        super(RandomStringAPI, self).__init__()

    def get(self):
        """Gets random strings"""
        args = self.reqparse.parse_args()
        # default params
        min = 10
        max = 20
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
        if min > 1000:
            min = 1000
        if max > 1000:
            max = 1000
        # set letters only or all chars
        allchar = string.ascii_letters
        if args.get('all') and args.get('all') is True:
            allchar = string.ascii_letters + string.punctuation + string.digits
        # list of strings
        strings = []
        # get the correct number of random strings
        for i in range(0, count):
            strings.append("".join(choice(allchar) for x in range(SystemRandom().randint(min, max))))
        # return strings
        return Response(json.dumps(strings),  mimetype='application/json')