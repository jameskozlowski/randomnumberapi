from flask import Flask
from flask_restful import Api
from randomnumberapi import RandomNumberAPI
from randomstringapi import RandomStringAPI
from randomuuidapi import RandomUUIDAPI

app = Flask(__name__)
api = Api(app)


api.add_resource(RandomNumberAPI, '/api/v1.0/random')
api.add_resource(RandomNumberAPI, '/api/v1.0/randomnumber')
api.add_resource(RandomStringAPI, '/api/v1.0/randomstring')
api.add_resource(RandomUUIDAPI, '/api/v1.0/randomuuid')
api.add_resource(RandomUUIDAPI, '/api/v1.0/uuid')


if __name__ == '__main__':
    app.debug = True
    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
