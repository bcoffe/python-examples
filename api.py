from resources.sample_control import SampleControl, SampleControls
from flask import Flask, jsonify, request
from flask.ext.restful import Api, abort, Resource
from flask.ext.cors import CORS
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

app = Flask(__name__)
api = Api(app)

api.add_resource(SampleControl, '/sample_control/<string:sample_id>')
api.add_resource(SampleControls, '/sample_control')

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=5000)
    IOLoop.instance().start()
