from polls.models import  import postgresql

class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == postgresql:
            return 'sqllite'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model == postgresql:
            return 'sqllite'
        return None