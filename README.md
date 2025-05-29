# TEMPLATE_RPA_PROJECT

This is a repository template with the structure of src layout for RPA projects.
It work with ***pdm***, ***cookiecutter*** and ***pytest***.

## Requirement

It is important you add cookiecutter to global pdm.

```bash
pdm self add cookiecutter
```

## Use

```bash
pdm init --cookiecutter https://github.com/Alfa-R2/TEMPLATE_RPA_PROYECT.git
cd your_project_name
pdm install
git init . 
```

## Structure

```text
    ├── .vscode
    │   ├── launch.json                    <- Necessary file to set the debug of the package.
    │   └── settings.json                  <- Necessary file to enable auto-import, set pytest and configure venv.
    │
    ├── config
    │   └── config.ini.example             <- An example file with parameters that your project need to work correctly.
    │
    ├── scripts
    │   └── run.bat                        <- A .bat file that able your project run in the terminal.
    │
    ├── secrets
    │   ├── bot_gsheets.json.example       <- Necessary file to store the credentials of google sheet account.
    │   └── client_gmail.json.example      <- Necessary file to store the credentials of google email account.
    │
    ├── src
    │   └── {{cookiecutter.package_name}}  <- Your package.
    |       ├── decorators                 <- A dir with useful decorators.
    |       ├── __init__.py
    |       ├── __main__.py             
    |       ├── config.py                  <- A file where we load the environment variables.
    |       ├── logger.py                  <- A file where we set the logger of loguru.
    |       └── paths.py                   <- A file where we set a class to manage the module's paths.
    |       
    ├── tests                              <- A test dir that works with pytest.
    │
    ├── .gitignore                         <- File to ignore unnecessary files.
    |
    ├── example.env                        <- Example file to set the environment variables.
    |
    ├── pyproject.toml                     <- File to set the properties of the project.
    |
    └── README.md                          <- Information about the project.
