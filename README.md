# {{ cookiecutter.project_slug }}

{{ cookiecutter.description }}

## Uso

```bash
pdm install
pdm run start
```

## Descriptions

### .vscode

- ***launch.json*** -> Necessary file to debug the src module

### config

- ***config.ini.example*** -> Optional file to init variables

### Scripts

- ***bot.bat*** -> Necessary file to start the src module (it can be modify)

### secrets

- ***bot_gsheets.json*** -> Necessary file to store the credentials of google sheet account (the content is provided for google cloud Console)
- ***client_gmail.json*** -> Necessary file to store the credentials of google email account (the content is provided for google cloud Console)

### src

- ***paths.py*** -> Class to manage the module's paths

### tests

- It works with pytest

### Other

- ***.gitignore*** -> File to ignore unnecessary files
- ***pyproject.toml*** -> File to manage the dependencies
- ***example.env*** -> File to manage the environment variables
