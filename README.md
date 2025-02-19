# TEMPLATE_RPA_PROYECT

## DIR descriptions

### .vscode

- ***launch.json*** -> Necessary file to debug the src module

### config

- ***config_log.json*** -> Necessary file to init the module's logger
- ***config.ini.example*** -> Optional file to init env variables

### Scripts

- ***bot.bat*** -> Necessary file to start the src module (it can be modify)
- ***venv.bat*** -> Necessary file to create a virtual environment

### secrets

- ***bot_gsheets.json*** -> Necessary file to store the credentials of google sheet account (the content is provided for google cloud Console)
- ***client_gmail.json*** -> Necessary file to store the credentials of google email account (the content is provided for google cloud Console)

### src

- ***logger*** -> DIR with the module's logger
- ***paths.py*** -> Class to manage the module's paths
