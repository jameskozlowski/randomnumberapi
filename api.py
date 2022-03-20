from flask import Flask, render_template
from flask_restful import Api
from randomnumberapi import RandomNumberAPI
from randomstringapi import RandomStringAPI
from randomuuidapi import RandomUUIDAPI
from randomredditnumberapi import RandomReditNumberAPI
app = Flask(__name__)
api = Api(app)


api.add_resource(RandomNumberAPI, '/api/v1.0/random', endpoint='random')
api.add_resource(RandomNumberAPI, '/api/v1.0/randomnumber', endpoint='randomnumber')
api.add_resource(RandomStringAPI, '/api/v1.0/randomstring', endpoint='randomstring')
api.add_resource(RandomUUIDAPI, '/api/v1.0/randomuuid', endpoint='randomuuid')
api.add_resource(RandomUUIDAPI, '/api/v1.0/uuid', endpoint='uuid')
api.add_resource(RandomReditNumberAPI, '/api/v1.0/randomredditnumber', endpoint='randomredditnumber')

@app.route("/")
def home():  
    return render_template('homepage.html')

if __name__ == '__main__':
    app.debug = True
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
