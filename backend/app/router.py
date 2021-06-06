
class BancoFirstRouter:

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # import pdb
        # pdb.set_trace()
        if db == 'banco_1':
            if app_label == 'firstapp':
                return True
            else:
                return False

class BancoLastRouter:
   
    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db == 'banco_2':
                if app_label == 'lastapp':
                    return True
                else:
                    return False