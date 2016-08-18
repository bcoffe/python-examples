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
        DynamoDBAccessor.__init__(self, 'positive', 'no_template', 'proficiency')

    def get_sample_control(self, sample_id):
        if sample_id is not None:
            return MOCK_SAMPLE_CONTROLS[sample_id] if sample_id in MOCK_SAMPLE_CONTROLS else None
        return MOCK_SAMPLE_CONTROLS

    def query_sample_controls(self, *query_parameters):
        parameters = list(query_parameters)
        # Put the query here based on parameters
        return parameters

