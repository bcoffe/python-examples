from flask.ext.restful import reqparse, Api, abort, Resource
from accessors.sample_control_accessor import SampleControlAccessor


parser = reqparse.RequestParser()
parser.add_argument('type', type=str)


class SampleControl(Resource):

    def get(self, sample_id):
        sample_control = SampleControlAccessor().get_sample_control(sample_id)
        return sample_control if sample_control is not None else \
            abort(404, message="Sample Control {} doesn't exist".format(sample_id))


class SampleControls(Resource):

    def get(self):
        args = parser.parse_args()
        if args['type']:
            return SampleControlAccessor().query_sample_controls(args)

        return SampleControlAccessor().get_sample_control(None)
