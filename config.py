import os 

class Config(object): 
    SECRET_KY = os.envoirn.get('SECRET_KY') or "secret_string"
