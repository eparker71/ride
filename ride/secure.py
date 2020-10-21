import os

# secure settings havebeen moved to ENV varibales 
# may not want to keep this file anymore
secure_settings = {
    "DJANGO_KEY" : os.environ.get('DJANGO_KEY'),
    "API_KEY" : os.environ.get('API_KEY'),
    "MAP_KEY" : os.environ.get('MAP_KEY'),
}

