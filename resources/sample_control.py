from flask_restful import abort, reqparse, Resource
from accessors.sample_control_accessor import SampleControlAccessor

# Notice there are 2 classes in this file. This is a little different than other languages because of the way
# python works with overriding method signatures.
# Replace later with marshmallow but for now this works

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=False)
parser.add_argument('site', type=str, required=False)
parser.add_argument('control_id', type=str, required=False)


class SampleControl(Resource):

    # Good example of sending back 404 "not found"
    def get(self):
        args = parser.parse_args()
        print args
        if args['control_id'] is not None:
            print "I'm in if"
            sample_control = SampleControlAccessor().query_sample_controls(args)
        else:
            print "I'm in else"
            sample_control = SampleControlAccessor().get_sample_controls()

        return sample_control if sample_control is not None else \
            abort(404, message="No sample controls meet the query parameters")

    def post(self):
        args = parser.parse_args()
        print args
        if args['control_id'] is not None:
            abort(400, message="Can not create a new sample control if id is passed in")
        elif args['type'] is not None and args['site'] is not None:
            return "Yeah you passed in the correct parameters to create a new sample control"

        abort(400, message="Must send in both a site and a type")
