
class BancoFirstRouter:
    database = 'banco_1'
    route_app_labels = {'firstapp'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.database
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.database
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == self.database and app_label in self.route_app_labels:
            return True

class BancoLastRouter:
    database = 'banco_2'
    route_app_labels = {'lastapp'}
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.database
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.database
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == self.database and app_label in self.route_app_labels:
            return True

    