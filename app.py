from resources.sample_control import SampleControl, SampleControls
from flask import Flask
from flask.ext.restful import Api
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

app = Flask(__name__)
api = Api(app)

# Notice that the class names are single or plural, but I choose to keep the routes all plural
# this was following a pattern I found on a blog. Its really just a matter of opinion. The goal
# is to make an API consistent for the user. So neither plural nor singular is 'grammatically' correct
# but we pick plural because it tends to be the favored practice.

api.add_resource(SampleControl, '/sample_controls/<string:sample_id>')
api.add_resource(SampleControl, '/sample_controls/<string:control_type>/<string:site>')
api.add_resource(SampleControls, '/sample_controls')

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=5000)
    IOLoop.instance().start()
