from dynamodb_accessor import DynamoDBAccessor

# Mocking what a database might have in the tables
MOCK_SAMPLE_CONTROLS = {
    'positive_1': {'type': 'positive', 'site':'mocha'},
    'positive_2': {'type': 'positive','site':'mocha'},
    'no_template_1': {'type': 'no_template','site':'mda'},
}


# this code should know nothing about flask or rest services
class SampleControlAccessor(DynamoDBAccessor):
    def __init__(self):
        DynamoDBAccessor.__init__(self, 'sample_control')

    def get_sample_controls(self):
        return MOCK_SAMPLE_CONTROLS

    # Just an empty function for example purposes
    def query_sample_controls(self, *query_parameters):
        parameters = query_parameters
        if 'control_id' in parameters:
            print "Control Id found in parameters"
            return None
        # TODO: Build the query here based on parameters
        return parameters

