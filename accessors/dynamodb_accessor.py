class DynamoDBAccessor(object):
    # example of one or more parameters being passed to a method notice the *
    def __init__(self, table_name, *additional_tables):
        self.table = table_name
        self.additional_tables = list(additional_tables)
        # put all the generic code to connect to dynmodb here
