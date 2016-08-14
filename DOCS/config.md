# Configuration options

The file config.py is holding config needed to run Sigma in an environment. When developing one would normally not need 
to specify any config. When deploying to a server the environment changes and WEBROOT must typically be specified. 

## Options
 - WEBROOT -- the folder path to the flask-files
 - SECRET_KEY -- Used for cryptating session data, must be unique and secret.

Sigma will run if none config file is present, it will then make one with a default config.
For now this means that the SECRET_KEY will be generated and written to config.py.
