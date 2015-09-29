from django.apps import AppConfig

class FrontmanConfig(AppConfig):
    name = 'frontman'
    verbose_name = "Frontman Web App"
    
    def ready(self):
        pass # startup code here