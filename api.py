from resources.sample_control import SampleControl
from resources.sample_controls import SampleControls
from flask import Flask
from flask.ext.restful import Api
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

app = Flask(__name__)
api = Api(app)

api.add_resource(SampleControl, '/sample_control/<string:sample_id>')
api.add_resource(SampleControls, '/sample_controls')

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=5000)
    IOLoop.instance().start()
