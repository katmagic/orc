class ValidatedUsers():
    '''
    A class to hold the connections who are
    currently connected and whose pseudonyms have been validated
    '''
    def __init__(self):
        #TODO work out communication by depending classes
        self.validated_users = dict()
    def add(self, connection, pseudonym):
        self.validated_users[pseudonym] = connection
        return
    def remove_pseudonym(self, pseudonym):
        return
    def remove_connection(self):
        return
    '''
    '''
    def remove_disconnected_users(self):
        # possible triggered by an event and may not need implementation
        return
        
        
        
#     TODO: find out how to declare and initialize a Dict. Write getters
# and setters. Write Boolean function to check
# if a connectino is validated

