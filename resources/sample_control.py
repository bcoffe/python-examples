from flask.ext.restful import abort, reqparse, Resource
from accessors.sample_control_accessor import SampleControlAccessor

# Notice there are 2 classes in this file. This is a little different than other languages because of the way
# python works with overriding method signatures.


class SampleControl(Resource):

    # Good example of sending back 404 "not found"
    def get(self, sample_id):
        sample_control = SampleControlAccessor().get_sample_control(sample_id)
        return sample_control if sample_control is not None else \
            abort(404, message="Sample Control {} doesn't exist".format(sample_id))

    def post(self, control_type, site):
        # do some work here to create a new sample control based on the type and site
        # SampleControlAccessor().create(control_type, site)
        return control_type

# Replace later with marshmallow but for now this works
parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=False)
parser.add_argument('site', type=str, required=False)


class SampleControls(Resource):

    def get(self):
        args = parser.parse_args()
        if args is not None:
            return SampleControlAccessor().query_sample_controls(args)

        return SampleControlAccessor().get_sample_control(None)

