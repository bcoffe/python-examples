from flask.ext.restful import reqparse, Api, abort, Resource
from accessors.sample_control_accessor import SampleControlAccessor

parser = reqparse.RequestParser()
parser.add_argument('type', type=str)
parser.add_argument('site', type=str)


class SampleControls(Resource):

    def get(self):
        args = parser.parse_args()
        if args['type']:
            return SampleControlAccessor().query_sample_controls(args)

        return SampleControlAccessor().get_sample_control(None)
